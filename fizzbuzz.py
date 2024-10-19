import math

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def exponentiation(base, exponent):
    return base ** exponent

def square_root(value):
    if value < 0:
        return "Cannot compute the square root of a negative number."
    return math.sqrt(value)

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. FizzBuzz")
        print("2. Exponentiation")
        print("3. Square Root")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            n = int(input("Enter a number for FizzBuzz: "))
            fizzbuzz(n)
        
        elif choice == '2':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = exponentiation(base, exponent)
            print(f"{base} raised to the power of {exponent} is {result}.")
        
        elif choice == '3':
            value = float(input("Enter a number to calculate the square root: "))
            result = square_root(value)
            print(f"The square root of {value} is {result}.")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")
