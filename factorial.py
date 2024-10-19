# factorial.py
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_valid_input(n):
    return isinstance(n, int) and n >= 0

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if is_valid_input(num):
                print(f"The factorial of {num} is {factorial(num)}")
                break  # Exit the loop if input is valid
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")
