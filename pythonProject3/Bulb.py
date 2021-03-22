from abc import ABC
from Goods import Goods
from Enums.TypeOfEnergyUse import *


class Bulb(Goods, ABC):
    def __init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date):
        Goods.__init__(self, TypeOfEnergyUse.ORDINARY, name, origin_country, producer, price, size_in_cm,
                       power_in_watts, expiration_date)

    def __str__(self):
        return (f"The type of lamp is {TypeOfEnergyUse.ORDINARY}\n"
                f"The name of Bulb is {self.name}\n"
                f"The origin country is {self.origin_country}\n"
                f"The producer is {self.producer}\n"
                f"The price is {self.price} hryvnia \n"
                f"The size in cm is {self.size_in_cm}\n"
                f"The power in watts is {self.power_in_watts}\n"
                f"The expiration date is {self.expiration_date}\n")
