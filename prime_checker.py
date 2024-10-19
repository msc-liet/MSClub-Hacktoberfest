def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    try:
        start = int(input("Enter the starting number of the range: "))
        end = int(input("Enter the ending number of the range: "))
        
        if start > end:
            print("Invalid range! The starting number must be less than or equal to the ending number.")
        else:
            prime_list = list_primes_in_range(start, end)
            if prime_list:
                print(f"Prime numbers between {start} and {end}: {prime_list}")
            else:
                print(f"There are no prime numbers in the range {start} to {end}.")
    except ValueError:
        print("Invalid input! Please enter valid integers.")
