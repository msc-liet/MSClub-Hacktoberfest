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

def exponentiate(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def floor_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a // b

if __name__ == "__main__":
    print("Basic Calculator is ready!")
    
    while True:
        try:
            operation = input("Enter operation (add, subtract, multiply, divide, exponentiate, modulus, floor_divide) or 'exit' to quit: ").strip().lower()
            if operation == 'exit':
                break

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if operation == 'add':
                print(f"Result: {add(a, b)}")
            elif operation == 'subtract':
                print(f"Result: {subtract(a, b)}")
            elif operation == 'multiply':
                print(f"Result: {multiply(a, b)}")
            elif operation == 'divide':
                print(f"Result: {divide(a, b)}")
            elif operation == 'exponentiate':
                print(f"Result: {exponentiate(a, b)}")
            elif operation == 'modulus':
                print(f"Result: {modulus(a, b)}")
            elif operation == 'floor_divide':
                print(f"Result: {floor_divide(a, b)}")
            else:
                print("Invalid operation. Please try again.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
