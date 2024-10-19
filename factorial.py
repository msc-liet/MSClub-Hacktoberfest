def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    while True:
        try:
            num = int(input("Enter a non-negative integer (or -1 to exit): "))
            if num == -1:
                print("Exiting the program.")
                break
            elif num < 0:
                print("Please enter a non-negative integer.")
            else:
                print(f"The factorial of {num} is {factorial(num)}")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

