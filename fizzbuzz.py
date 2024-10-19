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

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n <= 0:
                raise ValueError("The number must be positive.")
            break
        except ValueError as e:
            print(e)

    output = fizzbuzz(n)
    print("\n".join(output))
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

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n <= 0:
                raise ValueError("The number must be positive.")
            break
        except ValueError as e:
            print(e)

    output = fizzbuzz(n)
    print("\n".join(output))
