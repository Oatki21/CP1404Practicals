from Prac07.car import Car


def main():
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)
    bus = Car("bus",180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)


main()
