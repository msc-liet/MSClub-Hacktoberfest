def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    unit = input("Is this temperature in (C)elsius or (F)ahrenheit? ").strip().upper()
    
    if unit == 'C':
        print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    elif unit == 'F':
        print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
