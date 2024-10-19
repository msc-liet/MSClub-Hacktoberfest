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

def get_input():
    return int(input("Enter a number: "))

def is_fizz(num):
    return num % 3 == 0

def is_buzz(num):
    return num % 5 == 0

def custom_fizzbuzz(n, fizz_word="Fizz", buzz_word="Buzz"):
    for i in range(1, n + 1):
        output = ""
        if is_fizz(i):
            output += fizz_word
        if is_buzz(i):
            output += buzz_word
        if output:
            print(output)
        else:
            print(i)

if __name__ == "__main__":
    n = get_input()
    fizzbuzz(n)
    print("\nCustom FizzBuzz Output:")
    custom_fizzbuzz(n)
