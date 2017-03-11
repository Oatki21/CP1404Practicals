Looper = True
name = str(input("What is your name?"))
while Looper:
    choice = str(input("(He)llo\n(G)oodbye\n(Q)uit"))
    if choice.capitalize() == "H":
        print("Hello", name)
    elif choice.capitalize() == "G":
        print("Goodbye", name)
    elif choice.capitalize() == "Q":
        print("Finished.")
        Looper = False
    else:
        print("Invalid choice")



