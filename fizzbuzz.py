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

def custom_fizzbuzz(n, fizz_num=3, buzz_num=5):
    for i in range(1, n + 1):
        if i % fizz_num == 0 and i % buzz_num == 0:
            print("FizzBuzz")
        elif i % fizz_num == 0:
            print("Fizz")
        elif i % buzz_num == 0:
            print("Buzz")
        else:
            print(i)

def count_fizzbuzz(n):
    fizz_count = buzz_count = fizzbuzz_count = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_count += 1
        elif i % 3 == 0:
            fizz_count += 1
        elif i % 5 == 0:
            buzz_count += 1
    return fizz_count, buzz_count, fizzbuzz_count

def sum_fizzbuzz(n):
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == "__main__":
    n = 20
    print("Standard FizzBuzz:")
    fizzbuzz(n)
    
    print("\nCustom FizzBuzz (with default 3 and 5):")
    custom_fizzbuzz(n)

    fizz_count, buzz_count, fizzbuzz_count = count_fizzbuzz(n)
    print(f"\nCount of Fizz: {fizz_count}, Count of Buzz: {buzz_count}, Count of FizzBuzz: {fizzbuzz_count}")

    total_sum = sum_fizzbuzz(n)
    print(f"\nSum of all Fizz and Buzz numbers from 1 to {n}: {total_sum}")
