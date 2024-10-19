def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def main():
    """Main function to handle user input and conversions."""
    print("Welcome to the Temperature Converter!")
    
    while True:
        scale = input("Enter the scale (C for Celsius, F for Fahrenheit, Q to quit): ").strip().upper()

        if scale == 'Q':
            print("Exiting the temperature converter.")
            break

        if scale not in ['C', 'F']:
            print("Invalid scale. Please enter 'C' or 'F'.")
            continue

        try:
            temp = float(input(f"Enter temperature in {scale}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if scale == 'C':
            converted_temp = celsius_to_fahrenheit(temp)
            print(f"{temp:.2f}°C is {converted_temp:.2f}°F")
        else:
            converted_temp = fahrenheit_to_celsius(temp)
            print(f"{temp:.2f}°F 

