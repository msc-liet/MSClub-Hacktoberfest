# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print("Welcome to the Fibonacci sequence generator!")
    print("This program will generate the first 'n' terms of the Fibonacci sequence.")
    
    try:
        n = int(input("Enter the number of Fibonacci terms: "))
        if n < 0:
            raise ValueError("The number must be a non-negative integer.")
        print(f"Fibonacci sequence: {[num for num in fibonacci(n)]}")
    except ValueError as e:
        print(f"Invalid input: {e}")
