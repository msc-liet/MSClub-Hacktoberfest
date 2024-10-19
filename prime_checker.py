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
    while True:
        user_input = input("Enter a positive integer to check if it's prime (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        try:
            num = int(user_input)
            if num < 0:
                print("Please enter a non-negative integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        print(f"{num} is a prime number: {is_prime(num)}")

        # Ask for a range to list primes
        range_input = input("Would you like to see all prime numbers up to this number? (yes/no): ").strip().lower()
        if range_input == 'yes':
            primes = list_primes_in_range(2, num)
            print(f"Prime numbers between 2 and {num}: {primes}")
