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
    fizzbuzz(20)
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

def fizzbuzz_list(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

def count_fizzbuzz(n):
    fizz_count = sum(1 for i in range(1, n + 1) if i % 3 == 0)
    buzz_count = sum(1 for i in range(1, n + 1) if i % 5 == 0)
    fizzbuzz_count = sum(1 for i in range(1, n + 1) if i % 3 == 0 and i % 5 == 0)
    return fizz_count, buzz_count, fizzbuzz_count

if __name__ == "__main__":
    n = int(input("Enter the number up to which to run FizzBuzz: "))
    fizzbuzz(n)

    print("FizzBuzz List:", fizzbuzz_list(n))
    fizz_count, buzz_count, fizzbuzz_count = count_fizzbuzz(n)
    print(f"Count of Fizz: {fizz_count}, Count of Buzz: {buzz_count}, Count of FizzBuzz: {fizzbuzz_count}")
