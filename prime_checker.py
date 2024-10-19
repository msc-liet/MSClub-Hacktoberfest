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
    while True:
        user_input = input("Enter a number to check if it's prime (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Exiting the program.")
            break
        
        try:
            num = int(user_input)
            if num < 0:
                print("Negative numbers are not prime.")
            else:
                print(f"{num} is a prime number: {is_prime(num)}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        
        # Ask for range to list prime numbers
        range_input = input("Would you like to see prime numbers in a range? (y/n): ")
        if range_input.lower() == 'y':
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                if start > end:
                    print("Invalid range. Start should be less than or equal to end.")
                else:
                    primes = list_primes_in_range(start, end)
                    print(f"Prime numbers between {start} and {end}: {primes}")
            except ValueError:
                print("Invalid input. Please enter valid integers for the range.")
