# prime_checker.py
def is_prime(n:int)->bool:
    """Checks whether a number is prime.

    Args:
        n(int): The number to be checked for primality.

    Returns:
        Whether the number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}")
