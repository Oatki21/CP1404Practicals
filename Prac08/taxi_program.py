from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi


def main():
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    current_taxi = None
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = str(input(">>> ")).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis Avaliable:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print(current_taxi)
            print("Bill to date: ${:.2f}".format(bill))

        elif menu_choice == "d":
            current_taxi.start_fare()
            get_distance = int(input("Drive how far? "))
            current_taxi.drive(get_distance)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            bill = bill + current_taxi.get_fare()
            print("Bill to date: ${:.2f}".format(bill))
        else:
            print("Error, please enter a valid input.")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = str(input(">>> ")).lower()
    print("Total trip cost: ${}".format(bill))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
