def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_in_range(start, end):
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes

if __name__ == "__main__":
    num = int(input("Enter a number to check if it's prime: "))
    print(f"{num} is a prime number: {is_prime(num)}")

    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))

    if start > end:
        print("Invalid range. The starting number must be less than or equal to the ending number.")
    else:
        primes_in_range = list_primes_in_range(start, end)
        print(f"Prime numbers between {start} and {end}: {primes_in_range}")
