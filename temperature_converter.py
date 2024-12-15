# temperature_converter.py
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
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
