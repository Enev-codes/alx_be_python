FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    convert = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {convert}°C")

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    convert = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celsius}°C is {convert}°F")

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if unit.lower() != 'c' and unit.lower() != 'f':
            raise Exception
    except:
        print("Invalid temperature. Please enter a numeric value.")

    if unit.lower() == 'c':
        convert_to_fahrenheit(temp)
    if unit.lower() == 'f':
        convert_to_celsius(temp)


if __name__ == '__main__':
    main()
