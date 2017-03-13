def main():
    LOWER = 33
    UPPER = 127
    number = get_number(LOWER, UPPER)
    asciiNumber = chr(number)
    print("The character for {} is {}".format(number, asciiNumber))

    for i in range(LOWER, UPPER):
        print("{0:3} {1:>6}".format(i, chr(i)))

def get_number(LOWER, UPPER):
    Parameter = False
    number = 0
    character = str(input("Enter a character"))
    while character.isalpha() == False or len(character) != 1:
        print("Error! Enter a character")
        character = str(input("Enter a character"))
    asciiCharacter = ord(character)
    print("The ASCII code for {} is {}".format(character, asciiCharacter))
    while not Parameter:
        try:
            number = int(input("Enter a number between {} and {}:".format(LOWER, UPPER)))
            Parameter = True
        except ValueError or number > UPPER+1 or number < LOWER-1 or len(character) < 3 or len(character) < 0:
            print(("Invalid Number. Please enter a number between {} and {}:".format(LOWER, UPPER)))
    return number

main()

# Spacing
