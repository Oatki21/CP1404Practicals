from Prac07.guitar import Guitar


def main():
    guitars = []
    print("My Guitars!")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = input("Year: ")
        cost = input("Cost: $")
        guitars.append(Guitar(name,year,cost))

    print("These are my guitars:")
    for guitar in guitars:
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1,
                                                                   guitar.name, guitar.year, guitar.cost,
                                                                   Guitar.is_vintage(guitar)))


main()
