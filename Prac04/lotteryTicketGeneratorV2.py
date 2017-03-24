import random


def main():
    num_of_picks = int(input("How many quick picks? "))
    for i in range(num_of_picks):
        print("{:3} {:3} {:3} {:3} {:3} {:3}".format(random.randrange(0, 46), random.randrange(0, 46),
                                                     random.randrange(0, 46), random.randrange(0, 46),
                                                     random.randrange(0, 46), random.randrange(0, 46), ))


main()
