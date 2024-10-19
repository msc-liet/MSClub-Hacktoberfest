def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of Fibonacci terms: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"Fibonacci sequence: {fibonacci(n)}")
    except ValueError:
        print("Please enter a valid integer.")
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
