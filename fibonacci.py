def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def format_fibonacci(sequence):
    return ', '.join(map(str, sequence))

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    fib_sequence = fibonacci(n)
    formatted_output = format_fibonacci(fib_sequence)
    print(f"Fibonacci sequence: {formatted_output}")
