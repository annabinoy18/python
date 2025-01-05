#Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.
import math

def factorial_digits(n):
    # Compute factorial of n
    fact = math.factorial(n)
    
    # Convert the factorial result to a list of digits
    return [int(digit) for digit in str(fact)]

# Example Usage
n = 5
print(factorial_digits(n))  # Output: [1, 2, 0] (120)
