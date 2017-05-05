from Prac08.taxi import Car
from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi


def main():
    prius = Taxi("Prius 1", 100)
    prius.drive(40)
    print(prius)
    print("Current fare: ${}".format(prius.get_fare()))
    prius.start_fare()
    prius.drive(100)
    print(prius)
    print("Current fare: ${:.2f}".format(prius.get_fare()))
    Herbie = UnreliableCar("herbie", 100, 10.00)
    Herbie.drive(50)
    print(Herbie)
    Hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(Hummer)
    generic = SilverServiceTaxi("Generic", 200, 2)
    generic.start_fare()
    generic.drive(10)
    print("Current fare: ${:.2f}".format(generic.get_fare()))

main()
