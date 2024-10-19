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
            raise ValueError("Negative numbers are not allowed.")
        
        fib_sequence = fibonacci(n)
        # Format as a string
        fib_string = ', '.join(map(str, fib_sequence))
        print(f"Fibonacci sequence: {fib_string}")
        
    except ValueError as e:
        print(e)

