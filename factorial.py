# factorial.py
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num < 0:
                print("Please enter a positive integer.")
            else:
                print(f"The factorial of {num} is {factorial(num)}")
                break  # Exit the loop if valid input
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
