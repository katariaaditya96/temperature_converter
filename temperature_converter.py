def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def temperature_converter():
    print("🌡️ Temperature Converter")
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    choice = input("Enter your choice (1-6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        temp = float(input("Enter the temperature value: "))
        
        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")
        elif choice == '2':
            result = celsius_to_kelvin(temp)
            print(f"{temp}°C = {result:.2f}K")
        elif choice == '3':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")
        elif choice == '4':
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp}°F = {result:.2f}K")
        elif choice == '5':
            result = kelvin_to_celsius(temp)
            print(f"{temp}K = {result:.2f}°C")
        elif choice == '6':
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp}K = {result:.2f}°F")
    else:
        print("⚠️ Invalid choice. Please enter a number between 1 and 6.")

# Run the converter
temperature_converter()
