from Prac07.guitar import Guitar


def main():
    fender = Guitar("Fender", 1922, 5000)
    Air = Guitar("Air", 2011, 1)
    print(Guitar.get_age(fender))
    print(Guitar.get_age(Air))
    print(Guitar.is_vintage(fender))
    print(Guitar.is_vintage(Air))


main()
