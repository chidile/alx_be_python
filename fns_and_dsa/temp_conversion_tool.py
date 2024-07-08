# temp_conversion_tool.py

# Global variables to store conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FREEZING_POINT_FAHRENHEIT
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FREEZING_POINT_CELSIUS
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    choice = float(input("Enter the temperature to convert: "))
    temp_type = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))

    if temp_type == "F":
        fahrenheit = convert_to_celsius(choice)
        print(f"{choice}°F is {fahrenheit}°C")
    elif temp_type == "C":
        celsius = convert_to_fahrenheit(choice)
        print(f"{choice}°C is {celsius}°F")
    
    else:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()