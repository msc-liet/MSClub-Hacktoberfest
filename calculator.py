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
        return "Cannot take the square root of a negative number"
    return math.sqrt(a)

if __name__ == "__main__":
    print("Basic Calculator is ready!")
    
    while True:
        print("\nSelect operation:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Exponentiation (Power)")
        print("6: Square Root")
        print("7: Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in {'1', '2', '3', '4', '5', '6'}:
            if choice == '6':
                try:
                    num = float(input("Enter number: "))
                    result = square_root(num)
                    print(f"√{num} = {result}")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                continue
            
            try:
                num1 = float(input("Enter first number: "))
                if choice in {'5'}:
                    num2 = float(input("Enter second number (exponent): "))
                else:
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
        else:
            print("Invalid choice. Please select a valid operation.")
