"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


# __author__ = 'Lindsay Ward'
def main():
    menu = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(menu)
    choice = input(">>> ").upper()
    while choice.isalpha() is False or len(choice) != 1:
        print("Error! Enter a character")
        print(menu)
        choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            calculate_fahrenheit()
        elif choice == "F":
            calculate_celsius()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    result = ("Result: {:.2f} F".format(fahrenheit))
    return result


def calculate_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    result = ("Result: {:.2f} °".format(celsius))
    return result


main()
