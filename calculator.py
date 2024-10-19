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
        return "Cannot compute square root of a negative number"
    return math.sqrt(a)

def main():
    print("Basic Calculator")
    print("Operations: +, -, *, /, ^ (power), sqrt (square root)")
    
    while True:
        operation = input("Enter operation (+, -, *, /, ^, sqrt) or 'q' to quit: ")
        if operation.lower() == 'q':
            break
        
        if operation == 'sqrt':
            try:
                a = float(input("Enter number: "))
                result = square_root(a)
            except ValueError:
                print("Please enter a valid number.")
                continue
        else:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue
            
            if operation == '+':
                result = add(a, b)
            elif operation == '-':
                result = subtract(a, b)
            elif operation == '*':
                result = multiply(a, b)
            elif operation == '/':
                result = divide(a, b)
            elif operation == '^':
                result = power(a, b)
            else:
                print("Invalid operation.")
                continue

        print(f"Result: {result}")

if __name__ == "__main__":
    main()
