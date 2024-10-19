import argparse

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_sequence(sequence):
    """Print the Fibonacci sequence in a formatted way."""
    print("Fibonacci sequence:", ', '.join(map(str, sequence)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Fibonacci sequence.")
    parser.add_argument('n', type=int, nargs='?', default=10, 
                        help='Number of Fibonacci terms to generate (default: 10).')

    args = parser.parse_args()
    
    # Input validation
    if args.n <= 0:
        print("Please enter a positive integer.")
    else:
        fib_sequence = fibonacci(args.n)
        print_sequence(fib_sequence)

