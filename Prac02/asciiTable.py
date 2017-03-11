def main():
    LOWER = 33
    UPPER = 127
    number = get_number(LOWER, UPPER)
    asciiNumber = chr(number)
    print("The character for {} is {}".format(number, asciiNumber))

    for i in range(LOWER, UPPER):
        print("{0:3} {1:>6}".format(i, chr(i)))


def get_number(LOWER, UPPER):
    character = str(input("Enter a character"))
    while character.isalpha() == False or len(character) != 1:
        print("Error! Enter a character")
        character = str(input("Enter a character"))
    asciiCharacter = ord(character)
    print("The ASCII code for {} is {}".format(character, asciiCharacter))
    number = int(input("Enter a number between {} and {}:".format(LOWER, UPPER)))
    while number > UPPER or number < LOWER or len(character) != 1:
        #TODO simple error check for number
        number = int(input("Invalid Number. Please enter a number between {} and {}:".format(LOWER, UPPER)))
    return number


main()

# Spacing
