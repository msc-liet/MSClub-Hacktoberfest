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
# prime_checker.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_up_to(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}")

    limit = int(input("Enter a limit to list primes up to: "))
    print(f"Prime numbers up to {limit}: {list_primes_up_to(limit)}")

    print(f"The next prime after {num} is {next_prime(num)}")
