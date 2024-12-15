# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
def add (a,b):
    return a + b

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci sequence: {fibonacci(n)}")
