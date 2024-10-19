def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                raise ValueError("Factorial is not defined for negative numbers.")
            break
        except ValueError as e:
            print(e)

    # You can choose either the recursive or iterative approach
    print(f"The factorial of {num} (recursive) is: {factorial_recursive(num)}")
    print(f"The factorial of {num} (iterative) is: {factorial_iterative(num)}")
