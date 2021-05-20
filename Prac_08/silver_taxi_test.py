"""
SilverServiceTaxi class test
"""

from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxis("Hummer", 100, 2)
    taxi.drive(18)

    print(taxi)
    print('$', taxi.get_fare())

main()
