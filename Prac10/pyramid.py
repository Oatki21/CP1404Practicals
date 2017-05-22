def main():
    n = int(input("Enter the number of rows"))
    print("You'll need {} blocks".format(num_of_blocks(n)))


def num_of_blocks(n):
    if n > 0:
        return n + num_of_blocks(n - 1)
    else:
        return 0


main()
