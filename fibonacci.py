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
    print(f"Fibonacci sequence: {fibonacci(n)}")
# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_sum(n):
    sequence = fibonacci(n)
    return sum(sequence)

def fibonacci_even(n):
    sequence = fibonacci(n)
    even_numbers = [num for num in sequence if num % 2 == 0]
    return even_numbers

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci sequence: {fibonacci(n)}")
    print(f"Sum of Fibonacci sequence: {fibonacci_sum(n)}")
    print(f"Even numbers in Fibonacci sequence: {fibonacci_even(n)}")
