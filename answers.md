# CMPS 2200 Recitation 06
## Answers

**Name:**_Reid Miller_

**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

$W(n)=W(n-1)+W(n-2)+1$

$W(n)=O(2^n)$

- **3)**

$S(n) = S(n-1) + 1$

$S(n)=O(n)$

- **4)**

We can see that, in each loop, one index in the count list will increment by 1. In doing this, it fills the list up with previous
entries in the sequence. However, it is apparent that, while doing
this, it is calculating each entry from the bottom up. This means
that several repeat calculations are occurring.

- **6)**

For fib_top_down(i), the function will be recursively called at most 2i - 3 times (except for when i = 1). It is called n times
to break it down into its smallest pieces, then back up i - 3 times
to build back up starting at 2 and ending at i - 2.

$W(n)=O(n)$

$S(n)=O(n)$

- **8)**

$F_i$ will be read n times, as it loops n times to build up to
the desired Fibonacci value.

$W(n)=O(n)$

$S(n)=O(n)$