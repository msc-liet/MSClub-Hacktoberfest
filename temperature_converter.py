def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    scale = input("Is this in Celsius (C) or Fahrenheit (F)? ").strip().upper()

    if scale == 'C':
        print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    elif scale == 'F':
        print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
