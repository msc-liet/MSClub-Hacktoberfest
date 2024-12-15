def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    fib_sequence = fibonacci(n)
    # Formatting the output as a string
    print(f"Fibonacci sequence: {', '.join(map(str, fib_sequence))}")

