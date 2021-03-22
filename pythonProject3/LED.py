from abc import ABC
from Goods import Goods
from Enums.TypeOfEnergyUse import TypeOfEnergyUse


class LED(Goods, ABC):
    def __init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date,
                 color_of_shining):
        Goods.__init__(self, TypeOfEnergyUse.ENERGYSAVING, name, origin_country, producer, price, size_in_cm,
                       power_in_watts, expiration_date)
        self.color_of_shining = color_of_shining

    def __str__(self):
        return (f"The type of LED is {TypeOfEnergyUse.ENERGYSAVING}\n"
                f"The name of LED is {self.name}\n"
                f"The origin country is {self.origin_country}\n"
                f"The producer is {self.producer}\n"
                f"The price is {self.price} hryvnia \n"
                f"The size in cm is {self.size_in_cm}\n"
                f"The power in watts is {self.power_in_watts}\n"
                f"The expiration date is {self.expiration_date}\n"
                f"The type of color of shining is {self.color_of_shining}\n")

    def get_color_of_shining(self):
        return self.color_of_shining

    def set_color_of_shining(self, color_of_shining):
        self.color_of_shining = color_of_shining
