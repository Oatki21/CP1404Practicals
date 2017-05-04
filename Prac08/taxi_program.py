from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi


# def main():

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
print("Let's drive!")
menu_choice = " "
current_taxi = None
while menu_choice != "q":
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = str(input(">>> ")).lower()
    if menu_choice == "c":
        print("Taxis Avaliable:")
        for i, taxi in enumerate(taxis):
            print("{} - {}".format(i, taxi))
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
        print(current_taxi)

    elif menu_choice == "d":
        get_distance = int(input("Drive how far? "))
        current_taxi.drive(get_distance)
        print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))


# main()
