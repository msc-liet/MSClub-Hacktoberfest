# fizzbuzz.py
def fizzbuzz(n):
    """Prints the numbers from 1 to n. 
    For multiples of 3, print "Fizz" instead of the number. 
    For the multiples of 5, print "Buzz". 
    For numbers which are multiples of both 3 and 5, print "FizzBuzz".   
    
    Args:
      n(int): The upper limit of the range.
    """
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
