[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kdfTwECC)
# Midterm p1: Report on Analysis of Fibonacci  Series
* **Author**: Maggie Li
* **GitHub Repo**: https://github.com/CS5008Fall2025/midterm-report-maggiesomiakiraneu/tree/main
* **Semester**: Fall 2025
* **Languages Used**: c, update


## Overview
This report looks at how three different methods calculate the Fibonacci sequence: iterative, recursive, and dynamic programming. The Fibonacci sequence is an important idea in math and computer science, where each number is the sum of the two numbers before it.
#### what is the Fibonacci Sequence?
In Math, Fibonacci Sequence is defined as:

F(0)=0

F(1)=1

F(n)=F(n−1)+F(n−2) for n≥2

The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...


#### Algorithm Implementations and Complexity Analysis

The following table summarizes the time and space complexity for each algorithm:

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Iterative | O(n) | O(1) |
| Recursive | $O(2^n)$ | O(n) |
| Dynamic Programming | O(n) | O(n) |


#### 1. Iterative Algorithm
#### Here is the Pseudo code

```
 fib_iterative(n):
    IF n = 0 THEN
        RETURN 0
    IF n = 1 THEN
        RETURN 1
    
    prev2 =0 
    prev1 =1 
    
    FOR i FROM 2 TO n: #iterating from 2 to n here
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    END FOR
    
    RETURN current

```

#### Big O Analysis:
The iterative method uses one loop that runs from 2 to n. Each loop step does a few simple operations. 

- The loop runs (n - 1) times.
- Each loop step takes constant time O(1).
- Total time = T(n) = c × (n - 1) = O(n)

Space Complexity:

1. It uses only three variables (prev2, prev1, current) regardless of input size
Space
1. S(n) = O(1)

Therefore, Time: O(n), Space: O(1).


#### 2. Recursive Algorithm

**Pseudo Code:**
```
fib_recursive(n):
    IF n = 0 THEN
        RETURN 0
    IF n = 1 THEN
        RETURN 1
    
    RETURN fib_recursive(n-1) + fib_recursive(n-2)
```

#### Big O Analysis:

The recursive approach is different compared to iterative approcah. It calls itselfs in the function. It creates a binary tree of function calls, where each node represents a function call and branches to two more calls (except for base cases).


Time Complexity Derivation using Recurrence Relation.

#### Lower Bound:
To prove my Big(O), first, we will find the lower bound by approximating T(n-1) ≈ T(n-2), though T(n-1) ≥ T(n-2):

T(n) = T(n-1) + T(n-2) + c

= 2T(n-2) + c    //from the approximation T(n-1) ~ T(n-2)

= 2*(2T(n-4) + c) + c

= 4T(n-4) + 3c

= 8T(n-6) + 7c

= 2^k * T(n - 2k) + (2^k - 1)*c

Then, we will find the value of k for which n - 2k = 0, therefore k = n/2



T(n) = $2^{n/2}$ * T(0) + ($2^{n/2}$ - 1) * c

= $2^{n/2}$ * (1 + c) - c


Lower Bound: **T(n) ≥ $2^{n/2}$** 

#### Upper Bound:



T(n) = T(n-1) + T(n-2) + c

≤ 2T(n-1) + c //from the approximation T(n−2) to T(n−1)

= 2(2T(n-2) + c) + c

= 4T(n-2) + 3c

= 8T(n-3) + 7c

= $2^k$* T(n - k) + ($2^k$ - 1) * c


Let's find the value of k for which: n - k = 0, therefore k = n

T(n) = $2^n$ * T(0) + ($2^n$ - 1) * c

= $2^n$ * (1 + c) - c

Therefore: **T(n) ≤ $2^n$** (upper bound)


$2^{n/2}$ ≤ T(n) ≤ $2^n$

So, the time complexity is $O(2^n)$ or exponential.

**Space Complexity:**
- The call stack depth equals the longest path from root to leaf
- Maximum recursion depth = n (following the n-1 branch all the way down)
- Space: S(n) = O(n)

Therefore, **Time: $O(2^n)$, Space: O(n)**.


This method is simple to understand but very slow. For example, calculating F(40) takes around 1 trillion steps. It's too slow for most uses.

#### 3. Dynamic Programming Algorithm

**Pseudo Code:**
```
GLOBAL memo_table ← empty array of size MAX

fib_dp(n):
    IF n = 0 THEN
        RETURN 0
    IF n = 1 THEN
        RETURN 1
    
    IF memo_table[n] is not empty THEN
        RETURN memo_table[n]
    
    memo_table[n] =fib_dp(n-1) + fib_dp(n-2)
    RETURN memo_table[n]

```

**Big O Analysis:**

Dynamic programming saves results from earlier calculations.
When the function needs a value again, it just looks it up instead of recalculating it.

Time Complexity Derivation:
- Each unique value F(0) through F(n) is calculated only once
- After the first calculation, any repeated call just looks up the value in O(1) time
- There are n + 1 unique numbers
- Each calculation takes O(1) time (addition and storing in the table)
- T(n) = O(n)


Alternative Analysis:
- The recursion tree still exists, but repeated branches are removed
- The tree becomes more linear because each value is calculated only once
- Total function calls: approximately 2n - 1 because cached values return immediately

Space Complexity:
- Memoization table stores n + 1 values: S_table(n) = O(n)
- Call stack depth (worst case): O(n)
- Total space: S(n) = O(n)

Therefore, **Time: O(n), Space: O(n)**.

Dynamic programming is as fast as the iterative method O(n) but uses space O(n) instead of O(1). This trade-off is often worthwhile for problems where the recursive structure is more natural to express.





## Empirical Data & Discussion 


## Language Analysis


### Language 1: C



### Language 2: UPDATE



### Comparison and Discussion Between Experiences


## Conclusions / Reflection

## References

Big O, Big Efficiency : Recursion vs. Iteration Unveiled, Jun 2024, retrived in Oct 2025, from https://medium.com/@ireneselenam/big-o-big-efficiency-recursion-vs-iteration-unveiled-f0707501be5b

Solving Recurrences Example - Fibonacci (Recursion-Tree Method), 2017, retrived in Oct 2025, from https://www.youtube.com/watch?v=cDdSVCcugxg

Fibonacci Iterative vs. Recursive, Aug 2018, retrived in Oct 2025, from https://syedtousifahmed.medium.com/fibonacci-iterative-vs-recursive-5182d7783055

Dynamic Programming, https://www.cs.cmu.edu/~avrim/451f11/lectures/lect1006.pdf

Dynamic Programming (DP) Introduction, Aug 2025, retrived in Oct 2025 from https://www.geeksforgeeks.org/dsa/introduction-to-dynamic-programming-data-structures-and-algorithm-tutorials/