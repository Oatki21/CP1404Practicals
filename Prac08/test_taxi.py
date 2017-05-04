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
    herbie = UnreliableCar("herbie", 100, 10.00)
    herbie.drive(50)
    print(herbie)
    Hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(Hummer)
    Generic = SilverServiceTaxi("Generic", 200, 2)
    Generic.start_fare()
    Generic.drive(10)
    print("Current fare: ${:.2f}".format(Generic.get_fare()))

main()
