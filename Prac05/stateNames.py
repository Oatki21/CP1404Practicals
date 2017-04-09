"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


state = str(input("Enter short state: ")).upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = str(input("Enter short state: ")).upper()
