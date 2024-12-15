def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_user_input():
    """Prompts the user for a number and validates the input."""
    while True:
        try:
            num = int(input("Enter a positive integer (or type 'exit' to quit): "))
            if num < 0:
                print("Please enter a non-negative integer.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    while True:
        num = get_user_input()
        if num is None:
            break
        print(f"{num} is a prime number: {is_prime(num)}")
