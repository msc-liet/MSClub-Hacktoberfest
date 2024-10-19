def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)

def main():
    temp = float(input("Enter temperature: "))
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")

    # Additional conversions
    temp_kelvin = float(input("Enter temperature in Kelvin: "))
    print(f"{temp_kelvin} K is {kelvin_to_celsius(temp_kelvin)}°C")
    print(f"{temp_kelvin} K is {kelvin_to_fahrenheit(temp_kelvin)}°F")

    temp_c = float(input("Enter temperature in Celsius for Kelvin conversion: "))
    print(f"{temp_c}°C is {celsius_to_kelvin(temp_c)} K")

if __name__ == "__main__":
    main()
