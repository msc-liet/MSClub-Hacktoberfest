# prime_checker.py
# prime_checker.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}")
    
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    prime_numbers = primes_in_range(start, end)
    print(f"Prime numbers between {start} and {end}: {prime_numbers}")
