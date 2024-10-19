def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def get_positive_integer():
    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms: "))
            if n < 0:
                print("Please enter a non-negative integer.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    n = get_positive_integer()
    print(f"Fibonacci sequence: {fibonacci(n)}")
