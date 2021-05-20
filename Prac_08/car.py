"""
CP1404/CP5632 Practical
Car class
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car the distance provided, if the car has enough fuel. 
        If the distance is greater than the fuel, drive the car until the fuel runs out 
        and return the distance actually driven
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
