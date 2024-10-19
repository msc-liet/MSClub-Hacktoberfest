def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def get_positive_integer():
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num < 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    num = get_positive_integer()
    print(f"The factorial of {num} is {factorial(num)}")
