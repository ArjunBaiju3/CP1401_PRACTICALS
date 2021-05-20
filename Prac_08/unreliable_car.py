"""
UnreliableCar class
"""
from Prac_08.car import Car
from random import randint

"""Unreliable car class"""
class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_integer = randint(1, 100)
        if random_integer > self.reliability:
            distance = 0
        distance_travelled = super().drive(distance)
        return distance_travelled
