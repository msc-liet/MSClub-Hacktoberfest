# fizzbuzz.py
# fizzbuzz.py
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
    # Get user input for the range
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    fizzbuzz(start, end)
