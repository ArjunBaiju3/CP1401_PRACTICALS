
from Prac_08.taxi import Taxi


def main():
    """Test Taxi class."""

    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi)

    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)


main()
