def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_valid_input(n):
    return isinstance(n, int) and n > 0

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms (positive integer): "))
            if is_valid_input(n):
                fib_sequence = fibonacci(n)
                # Format the output as a string
                formatted_output = ', '.join(map(str, fib_sequence))
                print(f"Fibonacci sequence: {formatted_output}")
                break  # Exit the loop if input is valid
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
