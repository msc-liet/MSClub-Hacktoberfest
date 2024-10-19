# temperature_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    conversion_type = input("Choose conversion type (C to F or F to C): ").strip().lower()

    if conversion_type == "c to f":
        temp = float(input("Enter temperature in Celsius: "))
        print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    elif conversion_type == "f to c":
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    else:
        print("Invalid conversion type. Please choose 'C to F' or 'F to C'.")
