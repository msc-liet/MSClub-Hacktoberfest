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
    # Example usage
    while True:
        operation = input("Enter operation (+, -, *, /) or 'quit' to exit: ")
        if operation.lower() == 'quit':
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == '+':
            print(f"{a} + {b} = {add(a, b)}")
        elif operation == '-':
            print(f"{a} - {b} = {subtract(a, b)}")
        elif operation == '*':
            print(f"{a} * {b} = {multiply(a, b)}")
        elif operation == '/':
            print(f"{a} / {b} = {divide(a, b)}")
        else:
            print("Invalid operation. Please try again.")
