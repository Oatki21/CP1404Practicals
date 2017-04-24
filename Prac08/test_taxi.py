from Prac08.taxi import Car
from Prac08.taxi import Taxi


def main():

    prius = Taxi("Prius 1", 100, 1.20)
    prius.drive(40)
    print(prius)
    print("Current fare: ${}".format(prius.get_fare()))
    prius.start_fare()
    prius.drive(100)
    print(prius)
    print("Current fare: ${}".format(prius.get_fare()))


main()
