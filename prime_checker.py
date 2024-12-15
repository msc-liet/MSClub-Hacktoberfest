# prime_checker.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

if __name__ == "__main__":
    num = int(input("Enter a number to check if it's prime: "))
    print(f"{num} is a prime number: {is_prime(num)}")
    
    start = int(input("Enter the starting number for the prime list: "))
    end = int(input("Enter the ending number for the prime list: "))
    
    primes = list_primes_in_range(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")
