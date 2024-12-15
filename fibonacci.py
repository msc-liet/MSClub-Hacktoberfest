# fibonacci.py
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n < 0:
        print("Please enter a non-negative integer.")
        return []
    
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of Fibonacci terms: "))
        fib_sequence = fibonacci(n)
        # Format the output as a string
        fib_string = ', '.join(map(str, fib_sequence))
        print(f"Fibonacci sequence: {fib_string}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
