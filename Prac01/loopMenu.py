Looper = True
numberX = int(input("Enter x"))
numberY = int(input("Enter Y"))
while Looper:
    choice = str(input("1. Show the even numbers from x to y\n"
                       "2. Show the odd numbers from x to y\n"
                       "3. Show the squares from x to y\n"
                       "4. Exit the program"))
    if choice == "1":
        if numberX % 2 == 0:
            for i in range(numberX, numberY, 2,):
                print(i, end=' ')
        else:
            for i in range(numberX, numberY, 2,):
                print(i+1, end=' ')
    if choice == "2":
        if numberX % 2 == 0:
            for i in range(numberX, numberY, 2,):
                print(i+1, end=' ')
        else:
            for i in range(numberX, numberY, 2,):
                print(i, end=' ')
    if choice == "3":
        if numberX % 2 == 0:
            for i in range(numberX, numberY, 2,):
                print(i+1, end=' ')
        else:
            for i in range(numberX, numberY, 2,):
                print(i, end=' ')
    if choice.capitalize() == "4":
        print("Goodbye")
        Looper = False
    else:
        print("Invalid choice")
