"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
#__author__ = 'Lindsay Ward'
def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice.isalpha() == False or len(choice) != 1:
        print("Error! Enter a character")
        print(MENU)
        choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            calculate_fahrenheit()
        elif choice == "F":
            calculate_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def calculate_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    result = print("Result: {:.2f} F".format(fahrenheit))
    return result


def calculate_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    result = print("Result: {:.2f} °".format(celsius))
    return result



main()