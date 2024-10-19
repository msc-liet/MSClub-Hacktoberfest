def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def format_fibonacci(sequence):
    return ", ".join(map(str, sequence))

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms (positive integer): "))
            if n < 1:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    fib_sequence = fibonacci(n)
    formatted_output = format_fibonacci(fib_sequence)
    print(f"Fibonacci sequence ({n} terms): {formatted_output}")
