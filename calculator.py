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
    
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        if operation == 'exit':
            break
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if operation == '+':
            print(f"Result: {add(a, b)}")
        elif operation == '-':
            print(f"Result: {subtract(a, b)}")
        elif operation == '*':
            print(f"Result: {multiply(a, b)}")
        elif operation == '/':
            print(f"Result: {divide(a, b)}")
        else:
            print("Invalid operation.")
