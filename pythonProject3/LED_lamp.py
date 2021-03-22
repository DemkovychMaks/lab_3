from LED import LED
from Enums.TypeOfEnergyUse import TypeOfEnergyUse


class LedLamp(LED):
    def __init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date,
                 color_of_shining, type_of_shining):
        LED.__init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date,
                     color_of_shining)
        self.type_of_shining = type_of_shining

    def __str__(self):
        return (f"The type of Led lamp is {TypeOfEnergyUse.ENERGYSAVING}\n"
                f"The name of LED lamp is {self.name}\n"
                f"The origin country is {self.origin_country}\n"
                f"The producer is {self.producer}\n"
                f"The price is {self.price} hryvnia \n"
                f"The size in cm is {self.size_in_cm}\n"
                f"The power in watts is {self.power_in_watts}\n"
                f"The expiration date is {self.expiration_date}\n"
                f"The type of color of shining is {self.color_of_shining}\n"
                f"The type of shining is {self.type_of_shining}\n")

    def get_type_of_shining(self):
        return self.type_of_shining

    def set_type_of_shining(self, type_of_shining):
        self.type_of_shining = type_of_shining
