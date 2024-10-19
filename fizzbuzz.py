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

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_up_to(n):
    print("Prime numbers up to", n)
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")
    print()

def sum_of_multiples_of_3_and_5(n):
    total = sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)
    print(f"Sum of multiples of 3 and 5 up to {n}: {total}")
    return total

if __name__ == "__main__":
    fizzbuzz(20)
    print_primes_up_to(20)
    sum_of_multiples_of_3_and_5(20)
