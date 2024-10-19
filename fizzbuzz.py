# fizzbuzz.py
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

if __name__ == "__main__":
    fizzbuzz(20)
import math
import random

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
    if not numbers:
        return "No numbers provided"
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

def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers"
    return math.factorial(n)

def exponential(x):
    return math.exp(x)

def random_number(start, end):
    return random.randint(start, end)

def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def max_number(numbers):
    if not numbers:
        return "No numbers provided"
    return max(numbers)

def min_number(numbers):
    if not numbers:
        return "No numbers provided"
    return min(numbers)

def area_circle(radius):
    return math.pi * radius ** 2

def perimeter_circle(radius):
    return 2 * math.pi * radius

def area_rectangle(length, width):
    return length * width

def perimeter_rectangle(length, width):
    return 2 * (length + width)

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
    print("13. Factorial")
    print("14. Exponential")
    print("15. Random Number")
    print("16. Matrix Addition")
    print("17. Matrix Multiplication")
    print("18. Celsius to Fahrenheit")
    print("19. Maximum Number")
    print("20. Minimum Number")
    print("21. Area of Circle")
    print("22. Perimeter of Circle")
    print("23. Area of Rectangle")
    print("24. Perimeter of Rectangle")

    while True:
        choice = input("Enter choice (1-24) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in [str(i) for i in range(1, 25)]:
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
                elif choice == '13':
                    n = int(input("Enter a non-negative integer: "))
                    print(f"{n}! = {factorial(n)}")
                elif choice == '14':
                    x = float(input("Enter the exponent: "))
                    print(f"e^{x} = {exponential(x)}")
                elif choice == '15':
                    start = int(input("Enter start of range: "))
                    end = int(input("Enter end of range: "))
                    print(f"Random number between {start} and {end}: {random_number(start, end)}")
                elif choice == '16':
                    matrix1 = [[float(num) for num in input("Enter the first matrix row (space-separated): ").split()]]
                    matrix2 = [[float(num) for num in input("Enter the second matrix row (space-separated): ").split()]]
                    print("Result of Matrix Addition:", matrix_addition(matrix1, matrix2))
                elif choice == '17':
                    print("Matrix multiplication requires compatible matrices. Please input as a list of rows.")
                    matrix1 = []
                    rows = int(input("Enter number of rows for the first matrix: "))
                    for _ in range(rows):
                        row = list(map(float, input("Enter row (space-separated): ").split()))
                        matrix1.append(row)
                    rows = int(input("Enter number of rows for the second matrix: "))
                    matrix2 = []
                    for _ in range(rows):
                        row = list(map(float, input("Enter row (space-separated): ").split()))
                        matrix2.append(row)
                    print("Result of Matrix Multiplication:", matrix_multiplication(matrix1, matrix2))
                elif choice == '18':
                    celsius = float(input("Enter temperature in Celsius: "))
                    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
                elif choice == '19':
                    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
                    print(f"Maximum = {max_number(numbers)}")
                elif choice == '20':
                    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
                    print(f"Minimum = {min_number(numbers)}")
                elif choice == '21':
                    radius = float(input("Enter the radius of the circle: "))
                    print(f"Area of circle = {area_circle(radius)}")
                elif choice == '22':
                    radius = float(input("Enter the radius of the circle: "))
                    print(f"Perimeter of circle = {perimeter_circle(radius)}")
                elif choice == '23':
                    length = float(input("Enter length of the rectangle: "))
                    width = float(input("Enter width of the rectangle: "))
                    print(f"Area of rectangle = {area_rectangle(length, width)}")
                elif choice == '24':
                    length = float(input("Enter length of the rectangle: "))
                    width = float(input("Enter width of the rectangle: "))
                    print(f"Perimeter of rectangle = {perimeter_rectangle(length, width)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator
