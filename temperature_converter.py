# temperature_converter.py
def celsius_to_fahrenheit(c:float)->float:
    """Transform a Celsius temperature reading into its corresponding Fahrenheit value.
    
    Args:
        c(float): The temperature in Celsius.

    Returns:
        The equivalent temperature in Fahrenheit.
    """
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f:float)->float:
    """Transform a Fahrenheit temperature reading into its corresponding Celsius value.
    
    Args:
        f(float): The temperature in Fahrenheit.

    Returns:
        The equivalent temperature in Celsius.
    """
    return (f - 32) * 5/9

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
