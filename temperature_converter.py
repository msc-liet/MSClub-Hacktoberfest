# temperature_converter.py
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)

def kelvin_to_celsius(k):
    return k - 273.15

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
    print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
    
    kelvin_temp = float(input("Enter temperature in Kelvin: "))
    print(f"{kelvin_temp}K is {kelvin_to_celsius(kelvin_temp)}°C")
