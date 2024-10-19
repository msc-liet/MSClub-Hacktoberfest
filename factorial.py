# factorial.py

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_positive(n):
    return n >= 0

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    
    if is_positive(num):
        print(f"The factorial of {num} (recursive) is {factorial(num)}")
        print(f"The factorial of {num} (iterative) is {factorial_iterative(num)}")
    else:
        print("Please enter a non-negative number.")
