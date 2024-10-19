# calculator.py
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

if __name__ == "__main__":
    print("Basic Calculator is ready!")
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

def modulo(a, b):
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Cannot take the square root of a negative number"
    return math.sqrt(a)

def average(numbers):
    return sum(numbers) / len(numbers)

def logarithm(a, base=10):
    if a <= 0:
        return "Logarithm undefined for non-positive numbers"
    return math.log(a, base)

def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Power")
    print("7. Square Root")
    print("8. Average")
    print("9. Logarithm")
    print("10. Sine")
    print("11. Cosine")
    print("12. Tangent")

    while True:
        choice = input("Enter choice (1-12) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in [str(i) for i in range(1, 13)]:
            try:
                if choice in ['1', '2', '3', '4', '5', '6']:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    if choice == '1':
                        print(f"{a} + {b} = {add(a, b)}")
                    elif choice == '2':
                        print(f"{a} - {b} = {subtract(a, b)}")
                    elif choice == '3':
                        print(f"{a} * {b} = {multiply(a, b)}")
                    elif choice == '4':
                        print(f"{a} / {b} = {divide(a, b)}")
                    elif choice == '5':
                        print(f"{a} % {b} = {modulo(a, b)}")
                    elif choice == '6':
                        print(f"{a} ^ {b} = {power(a, b)}")
                elif choice == '7':
                    a = float(input("Enter a number: "))
                    print(f"√{a} = {square_root(a)}")
                elif choice == '8':
                    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
                    print(f"Average = {average(numbers)}")
                elif choice == '9':
                    a = float(input("Enter a number: "))
                    base = float(input("Enter the base (default is 10): ") or 10)
                    print(f"log_{base}({a}) = {logarithm(a, base)}")
                elif choice == '10':
                    angle = float(input("Enter angle in degrees: "))
                    print(f"sin({angle}) = {sine(angle)}")
                elif choice == '11':
                    angle = float(input("Enter angle in degrees: "))
                    print(f"cos({angle}) = {cosine(angle)}")
                elif choice == '12':
                    angle = float(input("Enter angle in degrees: "))
                    print(f"tan({angle}) = {tangent(angle)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
