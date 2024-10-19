def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

def main():
    num = int(input("Enter a number: "))
    
    print(f"{num} is a prime number: {is_prime(num)}")
    print(f"The next prime number after {num} is: {next_prime(num)}")
    
    if num > 1:
        print(f"The prime factors of {num} are: {prime_factors(num)}")
    else:
        print("Prime factors are not applicable for numbers less than or equal to 1.")

if __name__ == "__main__":
    main()
