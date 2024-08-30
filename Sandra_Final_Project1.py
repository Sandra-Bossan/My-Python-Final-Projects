#UNIT CONVERTER

def convert_units(value, unit1, unit2):
    
    unit_conversions = {
        'length': {
            'm': 1,
            'cm': 0.01,
            'km': 1000,
            'mm': 0.001
        },
        'mass': {
            'kg': 1,
            'g': 0.001,
            'mg': 0.000001,
            'tonne': 1000
        },
        'volume': {
            'l': 1,
            'ml': 0.001
        }
    }
    
    for unit_category in unit_conversions:
        if unit1 in unit_conversions[unit_category] and unit2 in unit_conversions[unit_category]:

            base_value = value * unit_conversions[unit_category][unit1]

            converted_value = base_value / unit_conversions[unit_category][unit2]
            return converted_value
    
    return None

def unit_converter():
    print("Welcome to my Unit Converter :)")
    print("Effortless Conversions Ahead!")

    while True:
        try:
            value = float(input("What value would you want to convert: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        print("\nWhat unit do you want to convert from?:")
        print("Options:")
        print("m (metres), cm (centimetres), km (kilometres), mm (millimetres)")
        print("kg (kilograms), g (grams), mg (milligrams), tonne (tonnes)")
        print("l (litres), ml (millilitres)")
        unit1 = input("Enter your choice: ").lower()

        print("\nWhat unit do you want to convert to?:")
        print("Options:")
        print("m (metres), cm (centimetres), km (kilometres), mm (millimetres)")
        print("kg (kilograms), g (grams), mg (milligrams), tonne (tonnes)")
        print("l (litres), ml (millilitres)")
        unit2 = input("Enter your choice: ").lower()

        answer = convert_units(value, unit1, unit2)

        if answer is not None:
            print(f"Okay...\n{value} {unit1} is equivalent to {answer} {unit2}")
        else:
            print("Invalid unit conversion. Please try again.")

        print("\nWhat would you like to do?")
        print("1. Continue converting")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            continue
        elif choice == "2":
            print("Thank you for using my Unit Converter :) Bye!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    unit_converter()