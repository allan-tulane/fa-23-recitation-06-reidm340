def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    print(counts)
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)
    
def fib_top_down(n, fibs):
    print(n, fibs)
    if (fibs[n] != -1):
        return fibs[n]
    else:
        if n == 1:
            fibs[1] = 1
            return 1
        elif n == 2:
            fibs[2] = 1
            return 1
        else:
            fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
            return fibs[n]

def fib_bottom_up(n):
    a = 1
    b = 0
    c = 0
    i = 1
    while (i < n):
        c = a + b
        b = a
        a = c
        i += 1
    return c

def fib_bottom_up_better(n):
    ###TODO
    pass


"""
n = 10
counts = [0] * (n+1)
fib_recursive(n, counts)
print(counts)
print(sum(counts))
"""

n = 2
fibs = [-1] * (n+1)
fib_top_down(n, fibs)
#print(fibs)

n = 10
fib_bottom_up(n)