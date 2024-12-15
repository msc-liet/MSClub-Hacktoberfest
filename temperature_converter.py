def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if scale == 'C':
        print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
    elif scale == 'F':
        print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
