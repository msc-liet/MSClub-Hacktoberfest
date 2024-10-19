def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of Fibonacci terms: "))
        if n < 0:
            print("Please enter a positive integer.")
        else:
            print(f"Fibonacci sequence: {list(fibonacci(n))}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
