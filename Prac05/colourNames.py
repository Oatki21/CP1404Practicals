"""Replica of stateNames except with different dictionary. Only error checking is for no response."""
COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "	#faebd7", "black": "#000000", "BlueViolet": "#8a2be2",
                "CadetBlue": "#5f9ea0", "coral": "#ff7f50", "CornflowerBlue": "#6495ed"}
colour = input("Enter a colour name: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ")
