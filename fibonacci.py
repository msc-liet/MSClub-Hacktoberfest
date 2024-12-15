def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def format_fibonacci_as_string(sequence):
    return ', '.join(map(str, sequence))

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    
    # Get the Fibonacci sequence as a list
    fib_sequence = fibonacci(n)
    
    # Ask user how they want the output to be formatted
    choice = input("Do you want the sequence as a (L)ist or (S)tring? ").strip().lower()
    
    if choice == 'l':
        print(f"Fibonacci sequence as list: {fib_sequence}")
    elif choice == 's':
        formatted_sequence = format_fibonacci_as_string(fib_sequence)
        print(f"Fibonacci sequence as string: {formatted_sequence}")
    else:
        print("Invalid choice. Showing the sequence as a list by default.")
        print(f"Fibonacci sequence as list: {fib_sequence}")
