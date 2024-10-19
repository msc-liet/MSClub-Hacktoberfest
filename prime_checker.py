def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

if __name__ == "__main__":
    num = int(input("Enter a number to check if it's prime: "))
    print(f"{num} is a prime number: {is_prime(num)}")
    
    # Range for listing prime numbers
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    primes_in_range = list_primes_in_range(start, end)
    
    if primes_in_range:
        print(f"Prime numbers between {start} and {end}: {primes_in_range}")
    else:
        print(f"No prime numbers found between {start} and {end}.")
