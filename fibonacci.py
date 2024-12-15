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
    fib_sequence_str = ', '.join(map(str, fib_sequence))
    print(f"Fibonacci sequence: {fib_sequence_str}")
