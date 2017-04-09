STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for state in STATE_NAMES:
    print("{:<4} is {:>4}".format(state,STATE_NAMES[state]))