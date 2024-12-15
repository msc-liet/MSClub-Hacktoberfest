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
import time

def fizzbuzz(n, fizz_word="Fizz", buzz_word="Buzz"):
    results = {}
    count_fizz = 0
    count_buzz = 0
    count_fizzbuzz = 0
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results[i] = fizz_word + buzz_word
            count_fizzbuzz += 1
        elif i % 3 == 0:
            results[i] = fizz_word
            count_fizz += 1
        elif i % 5 == 0:
            results[i] = buzz_word
            count_buzz += 1
        else:
            results[i] = i

    return results, count_fizz, count_buzz, count_fizzbuzz

def save_results_to_file(results, filename="fizzbuzz_results.txt"):
    with open(filename, 'w') as file:
        for number, result in results.items():
            file.write(f"{number}: {result}\n")
    print(f"Results saved to {filename}")

def main():
    n = int(input("Enter the range for FizzBuzz: "))
    fizz_word = input("Enter the word for Fizz: ")
    buzz_word = input("Enter the word for Buzz: ")
    
    start_time = time.time()  # Start timing
    results, count_fizz, count_buzz, count_fizzbuzz = fizzbuzz(n, fizz_word, buzz_word)
    execution_time = time.time() - start_time  # Calculate execution time
    
    # Print results
    for number, result in results.items():
        print(f"{number}: {result}")
    
    # Print counts
    print(f"\nCount of '{fizz_word}': {count_fizz}")
    print(f"Count of '{buzz_word}': {count_buzz}")
    print(f"Count of '{fizz_word + buzz_word}': {count_fizzbuzz}")
    
    # Save results to file
    save_results_to_file(results)
    
    # Print execution time
    print(f"\nExecution time: {execution_time:.6f} seconds")

if __name__ == "__main__":
    main()
