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

def next_prime(n):
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return list(set(factors))  # Return unique factors

def list_primes_up_to(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}")
    
    print(f"The next prime number after {num} is {next_prime(num)}")
    
    print(f"Prime factors of {num}: {prime_factors(num)}")
    
    limit = int(input("Enter a limit to list all prime numbers up to: "))
    print(f"Prime numbers up to {limit}: {list_primes_up_to(limit)}")
