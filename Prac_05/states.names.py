"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}

state_abbreviation = input("Enter short state: ").upper()
while state_abbreviation != "":
    if state_abbreviation in CODE_TO_NAME:
        print(state_abbreviation, "is", CODE_TO_NAME[state_abbreviation])
    else:
        print("Invalid short state")
    state_abbreviation = input("Enter short state: ").upper()

for state_abbreviation, state in CODE_TO_NAME.items():
    print('{} is {}'.format(state_abbreviation, CODE_TO_NAME[state_abbreviation]))
