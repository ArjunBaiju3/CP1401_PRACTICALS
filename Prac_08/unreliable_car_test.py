"""
UnreliableCar class testing
"""
from Prac_08.unreliable_car import UnreliableCar


def main():

    reliable_car = UnreliableCar("Good reliability", 100, 85)
    unreliable_car = UnreliableCar("Poor reliability", 100, 5)

    for i in range(1, 11):
        print("Drive car {}km:")
        print("{:12} drove {:2}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{:12} drove {:2}km".format(unreliable_car.name, unreliable_car.drive(i)))
        print("")

    print('Test drive result:', reliable_car)
    print('Test drive result:', unreliable_car)


main()
