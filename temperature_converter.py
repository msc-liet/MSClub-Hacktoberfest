# temperature_converter.py
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

if __name__ == "__main__":
    while True:
        try:
            temp = float(input("Enter temperature: "))
            unit = input("Enter unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

            if unit == 'C':
                print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
                print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
            elif unit == 'F':
                print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
                print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
            elif unit == 'K':
                print(f"{temp}K is {kelvin_to_celsius(temp)}°C")
                print(f"{temp}K is {kelvin_to_fahrenheit(temp)}°F")
            else:
                raise ValueError("Invalid unit. Please enter C, F, or K.")
            break  # Exit the loop after successful conversion
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
