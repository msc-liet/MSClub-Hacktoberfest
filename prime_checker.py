def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a positive integer (or type 'exit' to quit): "))
            if num < 1:
                raise ValueError("The number must be a positive integer.")
        except ValueError as e:
            if str(e) == "invalid literal for int() with base 10: 'exit'":
                print("Exiting the program. Goodbye!")
                break
            else:
                print(e)
                continue

        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
