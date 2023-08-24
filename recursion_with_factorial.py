"""Recursive function uses call stack. Let's look at this in action with the factorial function factorial(5) is written as 5!
and it's defined like this: 5! = 5*4*3*2*1. Similarly, factorial(3) is 3*2*1. Here's a recursive function to calculate 
the factorial of a number"""

def factorial(n):
    if n == 1:
        return 1
    else:
        print(n)
        return n*factorial(n-1)

print(factorial(6))

"""
Stack:
| n | 1 | ----- > returns 1
| n | 2 | ----- > returns 2*1   = 2
| n | 3 | ----- > returns 3*2   = 6
| n | 4 | ----- > returns 4*6   = 24
| n | 5 | ----- > returns 5*24  = 120 
| n | 6 | ----- > returns 6*120 = 720
"""