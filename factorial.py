def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    while True:
        user_input = input("Enter a positive integer (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Exiting the program.")
            break
        
        try:
            num = int(user_input)
            if num < 0:
                print("Please enter a positive integer.")
            else:
                print(f"The factorial of {num} is {factorial(num)}")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
