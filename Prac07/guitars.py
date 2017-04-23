from Prac07.guitar import Guitar


def main():
    count = 0
    guitars = []
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("My Guitars!")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1,
                                                                   guitar.name, guitar.year, guitar.cost,
                                                                   Guitar.is_vintage(guitar)))
        # enumerate returns a tuple basically adding a counter to an iterable


main()
