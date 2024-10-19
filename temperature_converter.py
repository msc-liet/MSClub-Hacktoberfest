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

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def display_conversion_menu():
    print("Temperature Converter Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kelvin to Celsius")
    print("4. Kelvin to Fahrenheit")
    print("5. Celsius to Kelvin")
    print("6. Fahrenheit to Kelvin")
    print("7. Batch Conversion")
    print("8. Exit")

def batch_conversion():
    temps = input("Enter temperatures separated by commas (e.g., '32, 100, 273.15'): ")
    temps = [float(t) for t in temps.split(',')]
    
    for temp in temps:
        print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
        print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
        print(f"{temp}K is {kelvin_to_celsius(temp)}°C")
        print(f"{temp}K is {kelvin_to_fahrenheit(temp)}°F")
        print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
        print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
        print()  # For better readability

if __name__ == "__main__":
    while True:
        display_conversion_menu()
        choice = input("Choose an option (1-8): ")
        
        if choice == '1':
            temp = float(input("Enter temperature in Celsius: "))
            print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
        elif choice == '2':
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
        elif choice == '3':
            temp = float(input("Enter temperature in Kelvin: "))
            print(f"{temp}K is {kelvin_to_celsius(temp)}°C")
        elif choice == '4':
            temp = float(input("Enter temperature in Kelvin: "))
            print(f"{temp}K is {kelvin_to_fahrenheit(temp)}°F")
        elif choice == '5':
            temp = float(input("Enter temperature in Celsius: "))
            print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
        elif choice == '6':
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
        elif choice == '7':
            batch_conversion()
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 8.")
