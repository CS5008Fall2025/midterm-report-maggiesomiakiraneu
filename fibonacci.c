#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <string.h>

#define MAX 100000
typedef uint64_t ull;

static ull dp_table[MAX];

ull fib_iterative(int n, ull *ops) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    ull prev2 = 0;
    ull prev1 = 1;
    ull current = 0;
    
    for (int i = 2; i <= n; i++) {
        (*ops)++;
        current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    
    return current;
}

ull fib_recursive(int n, ull *ops) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    (*ops)++;
    return fib_recursive(n - 1, ops) + fib_recursive(n - 2, ops);
}

ull fib_dp(int n, ull *ops) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    if (dp_table[n] != 0) {
        return dp_table[n];
    }
    
    (*ops)++;
    dp_table[n] = fib_dp(n - 1, ops) + fib_dp(n - 2, ops);
    return dp_table[n];
}

void init_dp_table() {
    memset(dp_table, 0, sizeof(dp_table));
}

double time_function(ull (*func)(int, ull*), int n, ull *ops, bool print_result) {
    struct timespec begin, end;
    
    *ops = 0;
    
    clock_gettime(CLOCK_MONOTONIC, &begin);
    
    ull result = func(n, ops);
    
    clock_gettime(CLOCK_MONOTONIC, &end);
    
    if (print_result) {
        printf("F(%d) = %llu\n", n, result);
    }
    
    return (end.tv_nsec - begin.tv_nsec) / 1000000000.0 + 
           (end.tv_sec - begin.tv_sec);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Error: At least one argument needed!\n");
        return 1;
    }
    
    const int n = atoi(argv[1]);
    int type = 3;
    bool print_result = false;
    
    if (argc > 2) {
        type = atoi(argv[2]);
    }
    if (argc > 3) {
        print_result = true;
    }
    
    ull ops;
    double time_elapsed;
    
    //need to print out the series for all cases
    //
    switch (type) {
        case 0:
            printf("Iterative Fibonacci\n");
            printf("Fibonacci Series from 1 to %d:\n", n);
            for (int i = 1; i <= n; i++) {
                ops = 0;
                time_elapsed = time_function(fib_iterative, i, &ops, false);
                ull result = fib_iterative(i, &ops);
                printf("F(%d) = %llu (Time: %f, Operations: %llu)\n", i, result, time_elapsed, ops);
            }
            break;
            
        case 1:
            printf("Recursive Fibonacci\n");
            printf("Fibonacci Series from 1 to %d:\n", n);
            for (int i = 1; i <= n; i++) {
                ops = 0;
                time_elapsed = time_function(fib_recursive, i, &ops, false);
                ull result = fib_recursive(i, &ops);
                printf("F(%d) = %llu (Time: %f, Operations: %llu)\n", i, result, time_elapsed, ops);
            }
            break;

        case 2:
            printf("Dynamic Programming Fibonacci\n");
            printf("Fibonacci Series from 1 to %d:\n", n);
            for (int i = 1; i <= n; i++) {
                init_dp_table(); //had the table outside the loop. fixed.
                ops = 0;
                time_elapsed = time_function(fib_dp, i, &ops, false);
                ull result = fib_dp(i, &ops); //called wrong function.fixed.
                printf("F(%d) = %llu (Time: %f, Operations: %llu)\n", i, result, time_elapsed, ops);
            }
            break;
            
        case 4:
            ops = 0;
            time_elapsed = time_function(fib_iterative, n, &ops, false);
            printf("%f,%llu,", time_elapsed, ops);
            
            init_dp_table();
            ops = 0;
            time_elapsed = time_function(fib_dp, n, &ops, false);
            printf("%f,%llu,-,-\n", time_elapsed, ops);
            break;
            
        case 3:
        default:
            ops = 0;
            time_elapsed = time_function(fib_iterative, n, &ops, false);
            printf("%f,%llu,", time_elapsed, ops);
            
            init_dp_table();
            ops = 0;
            time_elapsed = time_function(fib_dp, n, &ops, false);
            printf("%f,%llu,", time_elapsed, ops);
            
            ops = 0;
            time_elapsed = time_function(fib_recursive, n, &ops, false);
            printf("%f,%llu\n", time_elapsed, ops);
            break;
    }
    
    return 0;
}