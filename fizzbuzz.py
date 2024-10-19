# fizzbuzz.py

def fizzbuzz(n):
    for i in range(1, n + 1):
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
        limit = int(input("Enter a number for FizzBuzz limit: "))
        if limit < 1:
            print("Please enter a positive integer.")
        else:
            fizzbuzz(limit)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
