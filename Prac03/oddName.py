'''Oliver Atkinson'''
def main():
    name = get_name()
    frequency = get_frequency()
    print_loop(name,frequency)


def get_frequency():
    frequency = 0
    intCheck = False
    while not intCheck:
        try:
            frequency = int(input("Please enter a number"))
            intCheck = True
        except ValueError:
            print("Please enter a valid integer.")
    return frequency



def print_loop(name,frequency):
    for i in range(0, len(name), frequency):
        print(name[i], end=' ')


def get_name():
    name = str(input("What is your name"))
    while name == "" or  name.isalpha() == False:
        print("error")
        name = str(input("What is your name"))
    return name


main()