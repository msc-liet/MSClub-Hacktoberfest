def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms (non-negative integer): "))
            if n < 0:
                raise ValueError("The number must be non-negative.")
            break
        except ValueError as e:
            print(e)

    print(f"Fibonacci sequence: {fibonacci(n)}")
