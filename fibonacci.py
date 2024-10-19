def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

def sum_of_fibonacci(n):
    return sum(fibonacci(n))

def main():
    n = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci sequence (iterative): {fibonacci(n)}")
    print(f"Fibonacci sequence (recursive): {fibonacci_recursive(n)}")
    print(f"Sum of first {n} Fibonacci terms: {sum_of_fibonacci(n)}")

if __name__ == "__main__":
    main()
