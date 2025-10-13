import subprocess
import sys
import csv
import argparse

EXEC = "./fibonacci"
TIMEOUT = 60
OUT_DEFAULT = "fibonacci_run.csv"
OUT_FILE_TIME = "timings_"
OUT_FILE_OPS = "ops_"
CSV_HEADER = "N,Iterative,Dynamic Programming,Recursive"


class RecursionTimeoutError(Exception):
    """Raised when recursive algorithm times out"""
    pass


def run_single(n: int, typ: int) -> dict:
    try:
        command = f"{EXEC} {n} {typ}"
        results = subprocess.run(
            command.split(), 
            timeout=TIMEOUT, 
            capture_output=True, 
            text=True
        )
    except subprocess.TimeoutExpired:
        raise RecursionTimeoutError(
            f"Timeout of {TIMEOUT} seconds reached for N={n}"
        )
    
    if results.returncode != 0:
        raise Exception(f"Error running {command}: {results.stderr}")
    
    # Parse CSV output: time1,ops1,time2,ops2,time3,ops3
    results_line = results.stdout.strip().split(",")
    timings = []
    operations = []
    
    for i in range(0, len(results_line), 2):
        timings.append(results_line[i])
        operations.append(results_line[i + 1])
    
    return {"timings": timings, "operations": operations}


def save_to_csv(values: list, out_file: str, step: int):
    with open(out_file, "w", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(CSV_HEADER.split(","))
        
        for i, row in enumerate(values):
            n_value = i * step + 1
            row_with_n = [n_value] + row
            csv_writer.writerow(row_with_n)
    
    print(f"Saved to: {out_file}")


def main(n: int, step: int = 1, out_file: str = OUT_DEFAULT):
    run_type = 3
    results = {"timings": [], "operations": []}
    
    print(f"Running tests from 1 to {n} with step={step}")
    print(f"Timeout set to {TIMEOUT} seconds")
    print(f"Executable: {EXEC}")
    print("-" * 50)
    
    for i in range(1, n + 1, step):
        try:
            print(f"Testing N={i}...", end=" ")
            result = run_single(i, run_type)
            results["timings"].append(result["timings"])
            results["operations"].append(result["operations"])
            print("✓")
            
        except RecursionTimeoutError as e:
            print(f"⏱ Timeout - switching to iterative+DP only")
            run_type = 4
            try:
                result = run_single(i, run_type)
                results["timings"].append(result["timings"])
                results["operations"].append(result["operations"])
            except Exception as e2:
                print(f"Error: {e2}", file=sys.stderr)
                break
                
        except Exception as e:
            print(f"✗ Error: {e}", file=sys.stderr)
            break
    
    print("-" * 50)
    save_to_csv(results["operations"], OUT_FILE_OPS + out_file, step)
    save_to_csv(results["timings"], OUT_FILE_TIME + out_file, step)
    print("Data collection complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Fibonacci tests and collect performance data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Test C version up to N=100
  python3 test_runner.py 100 --step 10
  
  # Test Python version
  python3 test_runner.py 100 --step 10 --exec "python3 fibonacci.py"
  
  # Custom output and timeout
  python3 test_runner.py 50 --step 5 --out custom.csv --timeout 120
        """
    )
    
    parser.add_argument(
        "n", 
        type=int, 
        help="Maximum N value to test"
    )
    parser.add_argument(
        "--step", 
        type=int, 
        default=1, 
        help="Step size between tests (default: 1)"
    )
    parser.add_argument(
        "--out", 
        type=str, 
        default=OUT_DEFAULT,
        help=f"Output filename base (default: {OUT_DEFAULT})"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=TIMEOUT,
        help=f"Timeout in seconds (default: {TIMEOUT})"
    )
    parser.add_argument(
        "--exec",
        type=str,
        default=EXEC,
        help=f"Executable command (default: {EXEC})"
    )
    
    args = parser.parse_args()
    
    TIMEOUT = args.timeout
    EXEC = args.exec
    
    main(args.n, args.step, args.out)