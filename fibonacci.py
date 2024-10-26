# fibonacci.py
def fibonacci(n:int)->list[int]:
    """Returns Fibonacci sequence of a specified length.

    Args:
        n(int): The length of the sequence.

    Returns:
        The Fibonacci sequence of the specified length.
    """
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci sequence: {fibonacci(n)}")
