def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_of_list(numbers):
    return [factorial(num) for num in numbers]

def main():
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} (recursive) is {factorial(num)}")
    print(f"The factorial of {num} (iterative) is {factorial_iterative(num)}")
    
    numbers = list(map(int, input("Enter a list of numbers (separated by spaces): ").split()))
    print(f"Factorials of the list {numbers} are: {factorial_of_list(numbers)}")

if __name__ == "__main__":
    main()
