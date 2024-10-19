# prime_checker.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

def count_primes_in_range(start, end):
    return sum(1 for num in range(start, end + 1) if is_prime(num))

def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def are_twin_primes(a, b):
    return is_prime(a) and is_prime(b) and abs(a - b) == 2

def is_mersenne_prime(p):
    return is_prime(2**p - 1)

def goldbach_conjecture(even_number):
    if even_number <= 2 or even_number % 2 != 0:
        return "Input must be an even number greater than 2."
    for i in range(2, even_number):
        if is_prime(i) and is_prime(even_number - i):
            return f"{even_number} = {i} + {even_number - i}"

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Check if a number is prime")
        print("2. List prime numbers in a range")
        print("3. Count prime numbers in a range")
        print("4. Generate the first n prime numbers")
        print("5. Check if two numbers are twin primes")
        print("6. Check if a number is a Mersenne prime")
        print("7. Find two primes that sum to an even number (Goldbach's Conjecture)")
        print("8. Prime factorization of a number")
        print("9. Quit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            num = int(input("Enter a number: "))
            print(f"{num} is a prime number: {is_prime(num)}")
        
        elif choice == '2':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            primes = primes_in_range(start, end)
            print(f"Prime numbers between {start} and {end}: {primes}")
        
        elif choice == '3':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            count = count_primes_in_range(start, end)
            print(f"There are {count} prime numbers between {start} and {end}.")
        
        elif choice == '4':
            n = int(input("Enter the number of prime numbers to generate: "))
            primes = generate_primes(n)
            print(f"The first {n} prime numbers are: {primes}")
        
        elif choice == '5':
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            if are_twin_primes(a, b):
                print(f"{a} and {b} are twin primes.")
            else:
                print(f"{a} and {b} are not twin primes.")
        
        elif choice == '6':
            p = int(input("Enter a number to check for Mersenne prime (p): "))
            if is_mersenne_prime(p):
                print(f"2^{p} - 1 is a Mersenne prime.")
            else:
                print(f"2^{p} - 1 is not a Mersenne prime.")
        
        elif choice == '7':
            even_number = int(input("Enter an even number greater than 2: "))
            result = goldbach_conjecture(even_number)
            print(result)
        
        elif choice == '8':
            n = int(input("Enter a number to factor: "))
            factors = prime_factors(n)
            print(f"Prime factors of {n}: {factors}")
        
        elif choice == '9':
            print("Exiting the prime checker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
