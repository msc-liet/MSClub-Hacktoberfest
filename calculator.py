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
== 0:         return "Cannot divide by zero"     return a / b  if __name__ == "__main__":     print("Basic Calculator is ready!") add 2-3 functions
ChatGPT said:
ChatGPT
Here's the updated calculator.py file with 3 additional functions:

python
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
