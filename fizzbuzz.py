def fizzbuzz(n):
    """Prints the FizzBuzz sequence up to n."""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def get_positive_integer():
    """Prompts the user for a positive integer and validates the input."""
    while True:
        try:
            n = int(input("Enter the upper limit for FizzBuzz: "))
            if n <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    n = get_positive_integer()
    fizzbuzz(n)
