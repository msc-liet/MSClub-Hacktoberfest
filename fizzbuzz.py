def fizzbuzz(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def is_valid_input(n):
    return isinstance(n, int) and n > 0

if __name__ == "__main__":
    while True:
        try:
            start = int(input("Enter the starting number (positive integer): "))
            end = int(input("Enter the ending number (positive integer greater than starting number): "))
            
            if is_valid_input(start) and is_valid_input(end) and start < end:
                fizzbuzz(start, end)
                break  # Exit the loop if input is valid
            else:
                print("Please enter valid positive integers, and ensure the ending number is greater than the starting number.")
        except ValueError:
            print("Invalid input. Please enter valid positive integers.")
