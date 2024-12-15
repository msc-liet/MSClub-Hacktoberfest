# temperature_converter.py
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15

def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius."""
    return k - 273.15

def fahrenheit_to_kelvin(f):
    """Convert Fahrenheit to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

if __name__ == "__main__":
    print("Temperature Converter")
    print("Select the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    try:
        choice = int(input("Enter your choice (1-6): "))
        temp = float(input("Enter temperature: "))

        if choice == 1:
            print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
        elif choice == 2:
            print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
        elif choice == 3:
            print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
        elif choice == 4:
            print(f"{temp}K is {kelvin_to_celsius(temp)}°C")
        elif choice == 5:
            print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
        elif choice == 6:
            print(f"{temp}K is {kelvin_to_fahrenheit(temp)}°F")
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

