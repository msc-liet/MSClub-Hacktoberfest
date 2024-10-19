# prime_checker.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

def count_primes_up_to(n):
    return sum(1 for i in range(2, n + 1) if is_prime(i))

def check_multiple_numbers(numbers):
    return {num: is_prime(num) for num in numbers}

def largest_prime_factor(n):
    largest = None
    for i in range(2, n + 1):
        while n % i == 0:
            largest = i
            n //= i
    return largest

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes

def is_mersenne_prime(p):
    if is_prime(p):
        return is_prime(2**p - 1)
    return False

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}")
    
    # List of prime numbers in a range
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    print(f"Prime numbers between {start} and {end}: {primes_in_range(start, end)}")

    # Count prime numbers up to a given number
    count_num = int(input("Count prime numbers up to: "))
    print(f"Number of prime numbers up to {count_num}: {count_primes_up_to(count_num)}")
    
    # Check multiple numbers
    multiple_numbers = list(map(int, input("Enter numbers to check (comma-separated): ").split(',')))
    results = check_multiple_numbers(multiple_numbers)
    for num, is_prime_result in results.items():
        print(f"{num} is a prime number: {is_prime_result}")
    
    # Largest prime factor
    factor_num = int(input("Enter a number to find its largest prime factor: "))
    print(f"The largest prime factor of {factor_num} is: {largest_prime_factor(factor_num)}")

    # Generate primes using Sieve of Eratosthenes
    limit = int(input("Enter a limit to generate prime numbers: "))
    print(f"Prime numbers up to {limit}: {sieve_of_eratosthenes(limit)}")

    # Check if a number is a Mersenne prime
    p = int(input("Enter a number to check if it is a Mersenne prime: "))
    print(f"{p} is a Mersenne prime: {is_mersenne_prime(p)}")
