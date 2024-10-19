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
    print("Temperature Converter")
    print("Choose conversion type:")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("5: Fahrenheit to Kelvin")
    print("6: Kelvin to Fahrenheit")

    while True:
        choice = input("Enter the number of your choice (1-6): ")
        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("Invalid choice. Please enter a number from 1 to 6.")
            continue
        
        temp = float(input("Enter temperature: "))
        
        if choice == '1':
            print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
        elif choice == '2':
            print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
        elif choice == '3':
            print(f"{temp}°C is {celsius_to_kelvin(temp):.2f}K")
        elif choice == '4':
            print(f"{temp}K is {kelvin_to_celsius(temp):.2f}°C")
        elif choice == '5':
            print(f"{temp}°F is {fahrenheit_to_kelvin(temp):.2f}K")
        elif choice == '6':
            print(f"{temp}K is {kelvin_to_fahrenheit(temp):.2f}°F")
        
        break
