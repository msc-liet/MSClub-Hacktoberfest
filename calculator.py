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

def main():
    print("Basic Calculator is ready!")
    while True:
        try:
            operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
            if operation.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            
            if operation in ('+', '-', '*', '/'):
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                
                if operation == '+':
                    result = add(a, b)
                elif operation == '-':
                    result = subtract(a, b)
                elif operation == '*':
                    result = multiply(a, b)
                elif operation == '/':
                    result = divide(a, b)

                print(f"Result: {result}")
            else:
                print("Invalid operation. Please enter one of +, -, *, /.")
        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
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
