FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32)  * FAHRENHEIT_TO_CELSIUS_FACTOR
    return str(celsius) + "°C"

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return str(fahrenheit) + "°F"

try:
    temp = float(input("Enter the temperature to convert: "))
    conversion_function = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
    converted = ""

    if conversion_function == "C":
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°{conversion_function} is {converted}")
    elif conversion_function == "F":
        converted = convert_to_celsius(temp)
        print(f"{temp}°{conversion_function} is {converted}")
    else:
        print("Invalid unit please enter a valid unit (C/F)")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
