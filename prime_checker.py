def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Please enter a positive integer.")
        else:
            print(f"{num} is a prime number: {is_prime(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

