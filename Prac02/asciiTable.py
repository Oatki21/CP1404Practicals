def main():
    LOWER = 33
    UPPER = 127
    number = get_number(LOWER, UPPER)
    ascii_number = chr(number)
    print("The character for {} is {}".format(number, ascii_number))

    character = str(input("Enter a character"))
    while character.isalpha() is False or len(character) != 1:
        print("Error! Enter a character")
        character = str(input("Enter a character"))
    ascii_character = ord(character)
    print("The ASCII code for {} is {}".format(character, ascii_character))

    for i in range(LOWER, UPPER):
        print("{0:3} {1:>6}".format(i, chr(i)))


def get_number(lower, upper):
    while True:
        try:
            number = int(input("Enter a number between {} and {}:".format(lower, upper)))
            if number > upper or number < lower:
                print(("Invalid Number. Please enter a number between {} and {}:".format(lower, upper)))
            else:
                return number
        except ValueError:
            print(("Invalid Number. Please enter a number between {} and {}:".format(lower, upper)))

main()

# Spacing
