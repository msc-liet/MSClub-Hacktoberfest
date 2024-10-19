# factorial.py
def factorial(n):
    if n == 0 or n == 
def factorial(n):
    if n == 0 or n == 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter a number for factorial calculation: "))
    print(f"The factorial of {num} is {factorial(num)}")
    print(f"The factorial of {num} (iterative) is {factorial_iterative(num)}")

    prime_check_num = int(input("Enter a number to check if it's prime: "))
    print(f"{prime_check_num} is prime: {is_prime(prime_check_num)}")
