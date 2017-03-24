"""Predicament: The ascending order requirement indicates that it needs to be rows of lists using the sorted method.
The sample output doesn't have any square brackets and the integers need to be random on each line
(Can't repeat same list)
Can't think of a way to avoid repetition."""

import random


def main():
    random_row = [random.randrange(0, 46), random.randrange(0, 46), random.randrange(0, 46), random.randrange(0, 46),
                  random.randrange(0, 46), random.randrange(0, 46)]
    num_of_picks = int(input("How many quick picks? "))
    for i in range(num_of_picks):
        print(sorted(random_row))


main()
