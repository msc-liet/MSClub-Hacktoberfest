# hello_world.py
def greet():
    print("Hello, Hacktoberfest!")

if __name__ == "__main__":
    greet()
    # hello_world.py
def greet():
    print("Hello, Hacktoberfest!")

def introduce(name):
    print(f"Hello, {name}! Welcome to Hacktoberfest.")

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    greet()
    introduce("Alice")
    result_add = add_numbers(5, 3)
    result_multiply = multiply_numbers(4, 7)
    print(f"Addition Result: {result_add}")
    print(f"Multiplication Result: {result_multiply}")
    
