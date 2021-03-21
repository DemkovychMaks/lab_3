from LED import LED
from Enums.TypeOfEnergyUse import TypeOfEnergyUse


class Garland(LED):
    def __init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date,
                 color_of_shining, amount_of_diodes):
        LED.__init__(self, name, origin_country, producer, price, size_in_cm,
                     power_in_watts, expiration_date, color_of_shining)
        self.amount_of_diodes = amount_of_diodes

    def __str__(self):
        return (f"The type of lamp is {TypeOfEnergyUse.ENERGYSAVING}\n"
                f"The name of Garland is {self.name}\n"
                f"The origin country is {self.origin_country}\n"
                f"The producer is {self.producer}\n"
                f"The price is {self.price} hryvnia \n"
                f"The size in cm is {self.size_in_cm}\n"
                f"The power in watts is {self.power_in_watts}\n"
                f"The expiration date is {self.expiration_date}\n"
                f"The type of color of shining is {self.color_of_shining}\n"
                f"The amount of diodes is {self.amount_of_diodes}\n")

    def get_amount_of_diodes(self):
        return self.amount_of_diodes

    def set_amount_of_diodes(self, amount_of_diodes):
        self.amount_of_diodes = amount_of_diodes
