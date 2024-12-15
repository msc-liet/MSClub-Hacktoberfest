def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_in_range(start, end):
    """Generate a list of prime numbers in the given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    while True:
        try:
            start = int(input("Enter the starting number of the range: "))
            end = int(input("Enter the ending number of the range: "))
            
            if start > end:
                print("Error: Starting number must be less than or equal to ending number.")
                continue
            
            prime_numbers = list_primes_in_range(start, end)
            print(f"Prime numbers between {start} and {end}: {prime_numbers}")
            break  # Exit after successful execution
        except ValueError:
            print("Invalid input. Please enter valid integers.")
