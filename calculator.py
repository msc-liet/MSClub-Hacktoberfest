import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Cannot take square root of a negative number"
    return math.sqrt(a)

if __name__ == "__main__":
    print("Basic Calculator is ready!")

    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")

        choice = input("Choose an operation (1-7): ")

        if choice == '7':
            print("Exiting the calculator.")
            break

        if choice in {'1', '2', '3', '4', '5'}:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(a, b)}")
            elif choice == '2':
                print(f"Result: {subtract(a, b)}")
       
