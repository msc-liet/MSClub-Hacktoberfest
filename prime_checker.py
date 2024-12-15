# prime_checker.py
def is_prime(n):   # defines qualities to say if number prime is composite 
    if n <= 1:
        return False # ensures that numbers less than 1 aren't recognized as prime numbers, including negative numbers 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: #  ensures that the number doesn't have more than two factors, which would be the number itself and 1 for prime numbers. 
            return False # more than two factors means it's a composite number 
    return True 

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}") # runs number entered through defined prime number qualities to see if prime number or not and enters output 
