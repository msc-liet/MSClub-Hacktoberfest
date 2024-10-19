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
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
        
        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if operation in ('+', '-', '*', '/'):
            try:
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
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid operation. 
