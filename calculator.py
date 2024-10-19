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

memory = 0  # Variable to store memory value

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

def power(base, exponent):
    return base ** exponent

def square_root(a):
    if a < 0:
        return "Cannot take the square root of a negative number"
    return math.sqrt(a)

def modulo(a, b):
    if b == 0:
        return "Cannot perform modulo by zero"
    return a % b

def factorial(a):
    if a < 0:
        return "Cannot calculate factorial of a negative number"
    return math.factorial(a)

def exponential(a):
    return math.exp(a)

def store_in_memory(value):
    global memory
    memory = value
    return f"Stored {value} in memory."

def retrieve_from_memory():
    return memory

if __name__ == "__main__":
    print("Basic Calculator is ready!")

    while True:
        operation = input("Choose an operation (add, subtract, multiply, divide, power, sqrt, mod, factorial, exp, mem_store, mem_retrieve, exit): ").strip().lower()
        
        if operation == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif operation in ["add", "subtract", "multiply", "divide", "power", "mod"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: ")) if operation not in ["sqrt", "factorial"] else None
            
            if operation == "add":
                print(f"Result: {add(a, b)}")
            elif operation == "subtract":
                print(f"Result: {subtract(a, b)}")
            elif operation == "multiply":
                print(f"Result: {multiply(a, b)}")
            elif operation == "divide":
                print(f"Result: {divide(a, b)}")
            elif operation == "power":
                print(f"Result: {power(a, b)}")
            elif operation == "mod":
                print(f"Result: {modulo(a, b)}")
        elif operation == "sqrt":
            a = float(input("Enter number: "))
            print(f"Result: {square_root(a)}")
        elif operation == "factorial":
            a = int(input("Enter a non-negative integer: "))
            print(f"Result: {factorial(a)}")
        elif operation == "exp":
            a = float(input("Enter number: "))
            print(f"Result: {exponential(a)}")
        elif operation == "mem_store":
            value = float(input("Enter value to store in memory: "))
            print(store_in_memory(value))
        elif operation == "mem_retrieve":
            print(f"Retrieved from memory: {retrieve_from_memory()}")
        else:
            print("Invalid operation. Please try again.")
