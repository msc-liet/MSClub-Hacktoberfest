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

if __name__ == "__main__":
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        
        if start > end:
            print("Invalid range! The starting number must be less than or equal to the ending number.")
        else:
            fizzbuzz(start, end)
    except ValueError:
        print("Invalid input! Please enter valid integers.")
