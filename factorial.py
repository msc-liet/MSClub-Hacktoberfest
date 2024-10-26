# factorial.py
def factorial(n:int)->int:
    """Recursively calculate the factorial of a number.

    Args:
        n(int): The number whose factorial is to be calculated.

    Returns:
        The factorial of the specifed number.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {factorial(num)}")
