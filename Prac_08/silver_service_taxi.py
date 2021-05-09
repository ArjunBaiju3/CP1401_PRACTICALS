"""
SilverServiceTaxi class
"""

from Prac_08.taxi import Taxi


class SilverServiceTaxis(Taxi):

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    flagfall = 4.50

    def get_fare(self):
        return self.flagfall + super().get_fare()

    def __str__(self):
        return "{} plus flagfall of $ {:.2f}"\
            .format(super().__str__(), self.flagfall)
