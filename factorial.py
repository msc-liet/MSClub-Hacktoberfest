# factorial.py
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                raise ValueError("The number must be non-negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    print(f"The factorial of {num} is {factorial(num)}")
