from enum import Enum
from functools import lru_cache
import argparse
import sys
import time

sys.setrecursionlimit(100000)

ops_counter = 0


class FibType(Enum):
    ITERATIVE = 0
    RECURSIVE = 1
    DP = 2
    ALL = 3
    ITERATIVE_DP_TOGETHER = 4


def fib_iterative(n: int) -> int:
    global ops_counter
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev2 = 0  # F(0)
    prev1 = 1  # F(1)
    current = 0
    
    for i in range(2, n + 1):
        ops_counter += 1
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return current


def fib_recursive(n: int) -> int:
    global ops_counter
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    ops_counter += 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache(maxsize=None)
def fib_dp(n: int) -> int:
    global ops_counter
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    ops_counter += 1
    return fib_dp(n - 1) + fib_dp(n - 2)


def run_and_time(func, n: int, print_result: bool = False) -> tuple:
    global ops_counter
    ops_counter = 0
    
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    
    if print_result:
        print(f"F({n}) = {result}")
    
    return end - start, ops_counter


def main(n: int, algo: FibType, print_result: bool):
    if algo == FibType.ITERATIVE:
        print("Iterative Fibonacci")
        print(f"Fibonacci Series from 1 to {n}:")
        for i in range(1, n + 1):
            elapsed_time, ops = run_and_time(fib_iterative, i, False)
            result = fib_iterative(i)
            print(f"F({i}) = {result} (Time: {elapsed_time:.6f}, Operations: {ops})")
        
    elif algo == FibType.RECURSIVE:
        print("Recursive Fibonacci")
        print(f"Fibonacci Series from 1 to {n}:")
        for i in range(1, n + 1):
            elapsed_time, ops = run_and_time(fib_recursive, i, False)
            result = fib_recursive(i)
            print(f"F({i}) = {result} (Time: {elapsed_time:.6f}, Operations: {ops})")
        
    elif algo == FibType.DP:
        print("Dynamic Programming Fibonacci")
        print(f"Fibonacci Series from 1 to {n}:")
        for i in range(1, n + 1):
            fib_dp.cache_clear()
            elapsed_time, ops = run_and_time(fib_dp, i, False) //need to confirm with professor about the print msg
            result = fib_dp(i)
            print(f"F({i}) = {result} (Time: {elapsed_time:.6f}, Operations: {ops})")
        
    elif algo == FibType.ITERATIVE_DP_TOGETHER:
        time1, ops1 = run_and_time(fib_iterative, n)
        
        fib_dp.cache_clear()
        time2, ops2 = run_and_time(fib_dp, n)
        
        print(f"{time1:.6f},{ops1},{time2:.6f},{ops2},-,-")
        
    elif algo == FibType.ALL:
        time1, ops1 = run_and_time(fib_iterative, n)
        
        fib_dp.cache_clear()
        time2, ops2 = run_and_time(fib_dp, n)
        
        time3, ops3 = run_and_time(fib_recursive, n)
        
        print(f"{time1:.6f},{ops1},{time2:.6f},{ops2},{time3:.6f},{ops3}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate Fibonacci numbers using different algorithms"
    )
    parser.add_argument(
        "n", 
        type=int, 
        help="The nth Fibonacci number to calculate"
    )
    parser.add_argument(
        "algo",
        type=int,
        nargs='?',
        choices=[0, 1, 2, 3, 4],
        default=FibType.ALL.value,
        help="Algorithm type: 0=iterative, 1=recursive, 2=dp, 3=all, 4=iterative+dp"
    )
    parser.add_argument(
        "--print",
        action="store_true",
        default=False,
        help="Print the Fibonacci result"
    )
    
    args = parser.parse_args()
    algo = FibType(args.algo)
    main(args.n, algo, args.print)
