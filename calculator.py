import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def exponentiate(base, exponent):
    return base ** exponent

def square_root(value):
    if value < 0:
        return "Cannot take the square root of a negative number"
    return math.sqrt(value)

if __name__ == "__main__":
    print("Basic Calculator is ready!")
