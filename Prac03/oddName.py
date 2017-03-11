'''Oliver Atkinson'''
def main():
    name = get_name()
    frequency = get_frequency()
    print_loop(name,frequency)


def get_frequency():
    frequency = int(input("What's the frequency of the letters?"))
    # TODO ERROR CHECK INT
    return frequency


def print_loop(name,frequency):
    for i in range(0, len(name), frequency):
        print(name[i], end=' ')


def get_name():
    name = str(input("What is your name"))
    if name == "" or name != name.isalpha():
        print("error")
        str(input("What is your name"))
    return name


main()