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
    while True:
        try:
            start = int(input("Enter the start of the range (integer): "))
            end = int(input("Enter the end of the range (integer): "))
            if start > end:
                print("Start must be less than or equal to end.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    fizzbuzz(start, end)
