# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci sequence: {fibonacci(n)}")
thon
Copy code
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

def modulus(a, b):
    return a % b

def exponentiate(a, b):
    return a ** b

def floor_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a // b

if __name__ == "__main__":
    print("Basic Calculator is ready!")
