# factorial.py
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {factorial(num)}")
def factorial_recursive(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = n * factorial_recursive(n - 1, memo)
    return memo[n]

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_of_list(numbers):
    return [factorial_recursive(num) for num in numbers]

def is_valid_input(n):
    return isinstance(n, int) and n >= 0

def factorial_of_range(start, end):
    return {i: factorial_recursive(i) for i in range(start, end + 1)}

def explain_factorial(n):
    steps = [f"{i}" for i in range(n, 0, -1)]
    explanation = f"{n}! = " + " * ".join(steps) + " = " + str(factorial_recursive(n))
    return explanation

if __name__ == "__main__":
    num = int(input("Enter a non-negative integer: "))
    
    if is_valid_input(num):
        print(f"The factorial of {num} (recursive) is {factorial_recursive(num)}")
        print(f"The factorial of {num} (iterative) is {factorial_iterative(num)}")
        
        # Calculate factorial for a list of numbers
        numbers = list(map(int, input("Enter a list of non-negative integers (comma-separated): ").split(',')))
        if all(is_valid_input(n) for n in numbers):
            print(f"Factorials of the list: {factorial_of_list(numbers)}")
        else:
            print("All numbers in the list must be non-negative integers.")
        
        # Calculate factorial for a range
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if is_valid_input(start) and is_valid_input(end) and start <= end:
            print(f"Factorials of numbers from {start} to {end}: {factorial_of_range(start, end)}")
        else:
            print("Invalid range. Please ensure both numbers are non-negative integers and the start is less than or equal to the end.")

        # Explain the factorial calculation
        print(explain_factorial(num))
    else:
        print("Please enter a valid non-negative integer.")
