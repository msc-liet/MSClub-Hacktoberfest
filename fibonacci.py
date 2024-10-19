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
    format_choice = input("Output as list or formatted string (type 'list' or 'string'): ").strip().lower()

    fib_sequence = fibonacci(n)

    if format_choice == 'list':
        print(f"Fibonacci sequence: {fib_sequence}")
    elif format_choice == 'string':
        formatted_string = ', '.join(str(num) for num in fib_sequence)
        print(f"Fibonacci sequence: {formatted_string}")
    else:
        print("Invalid choice. Please type 'list' or 'string'.")
