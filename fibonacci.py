# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_nth(n):
    if n < 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci sequence: {fibonacci(n)}")

    nth = int(input("Enter the position to get the nth Fibonacci number: "))
    print(f"The {nth}th Fibonacci number is: {fibonacci_nth(nth)}")

    check_num = int(input("Enter a number to check if it's in the Fibonacci sequence: "))
    print(f"{check_nu
