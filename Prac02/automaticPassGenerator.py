SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"

def main():
    passLength = int(input("What's the length of your password?"))
    numLower = int(input("How many lowercase letters are required?"))
    numUpper = int(input("How many uppercase letters are required?"))
    numNumeric = int(input("How many numbers are required?"))
    numSepcial = int(input("How many special characters are required?"))

def is_valid_password(password):
    # TODO: if length is wrong, return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    for character in password:
        # TODO: count each kind of character
        if character.islower():
            count_lower = count_lower + 1
        elif character.isupper():
            count_upper = count_upper + 1
        elif character.isdigit():
            count_digit = count_digit + 1
        elif character in SPECIAL_CHARACTERS:
            count_special = count_special + 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0 or count_special == 0:
        return False


    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those and return False if it's zero

    # if we get here (without having returned False), then the password must be valid

    return True

main()