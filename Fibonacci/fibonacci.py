"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    first = 0
    second = 1
    next = first + second

    for i in range(2, position):
        first = second
        second = next
        next = first + second

    return next

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
