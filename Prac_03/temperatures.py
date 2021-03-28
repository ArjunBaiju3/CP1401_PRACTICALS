"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = conversion_celsius(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = conversion_fahrenheit(fahrenheit)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

"Converting celsius to fahrenheit"
def conversion_celsius(celsius):
    return celsius * 9.0 / 5 + 32

"Converting fahrenheit to celsius"
def conversion_fahrenheit(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

main()