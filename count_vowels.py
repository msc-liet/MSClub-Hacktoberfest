# count_vowels.py
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Number of vowels in '{string}': {count_vowels(string)}")
# hello_world.py

def greet():
    print("Hello, Hacktoberfest!")

def ask_participation():
    print("Are you participating in Hacktoberfest?")

def share_resources():
    print("Check out the official website for resources: https://hacktoberfest.com")

def say_goodbye():
    print("Goodbye! See you at Hacktoberfest!")

if __name__ == "__main__":
    greet()
    ask_participation()
    share_resources()
    say_goodbye()
