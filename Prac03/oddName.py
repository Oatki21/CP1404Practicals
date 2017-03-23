'''Oliver Atkinson'''


def main():
    name = get_name()
    frequency = get_frequency()
    print_loop(name, frequency)


def get_frequency():
    frequency = 0
    int_check = False
    while not int_check:
        try:
            frequency = int(input("Please enter a number"))
            int_check = True
        except ValueError:
            print("Please enter a valid integer.")
    return frequency


def print_loop(name, frequency):
    for i in range(0, len(name), frequency):
        print(name[i], end=' ')


def get_name():
    name = str(input("What is your name"))
    while name == "" or name.isalpha() == False:
        print("Error")
        name = str(input("What is your name"))
    return name


main()
