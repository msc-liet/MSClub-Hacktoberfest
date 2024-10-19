# temperature_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
    print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
