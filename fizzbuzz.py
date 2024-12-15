# fizzbuzz.py
def fizzbuzz(n):
    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results

def count_fizzbuzz(n):
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_count += 1
        elif i % 3 == 0:
            fizz_count += 1
        elif i % 5 == 0:
            buzz_count += 1
    return fizz_count, buzz_count, fizzbuzz_count

def fizzbuzz_list(n):
    results = fizzbuzz(n)
    print("FizzBuzz results:", results)

if __name__ == "__main__":
    n = 20
    fizzbuzz_list(n)
    fizz_count, buzz_count, fizzbuzz_count = count_fizzbuzz(n)
    print(f"Occurrences - Fizz: {fizz_count}, Buzz: {buzz_count}, FizzBuzz: {fizzbuzz_count}")
