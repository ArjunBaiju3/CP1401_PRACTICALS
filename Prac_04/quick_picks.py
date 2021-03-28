import random

#constants
nos_per_line = 6
min_number = 1
max_number = 45

def main():

    no_of_quick_picks = int(input("How many quick picks? "))
    while no_of_quick_picks <=0:
        print("Invalid number, please enter a valid amount")
        no_of_quick_picks = int(input("How many quick picks? "))

    for i in range(no_of_quick_picks):
        quick_pick = []
        for j in range(nos_per_line):
            number = random.randint(min_number, max_number)
            while number in quick_pick:
                number = random.randint(min_number, max_number)
            quick_pick.append(number)
        quick_pick.sort()
        #formatting numbers
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()