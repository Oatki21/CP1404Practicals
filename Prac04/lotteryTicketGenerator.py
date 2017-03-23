import random
def main():
    random_num = [random.randrange(0,46),random.randrange(0,46),random.randrange(0,46),random.randrange(0,46),random.randrange(0,46),random.randrange(0,46)]
    num_of_picks = int(input("How many quick picks? "))
    for i in range(num_of_picks):
        print (sorted(random_num))






main()