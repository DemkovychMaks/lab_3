from LED import LED
from Enums.TypeOfEnergyUse import TypeOfEnergyUse


class SolarPanel(LED):
    def __init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date,
                 color_of_shining, capacity, production_of_energy_per_day):
        LED.__init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date,
                     color_of_shining)
        self.capacity = capacity
        self.production_of_energy_per_day = production_of_energy_per_day
        self.type_of_lamp = TypeOfEnergyUse.SOLARPANEL

    def __str__(self):
        return (f"The type of LED is {TypeOfEnergyUse.SOLARPANEL}\n"
                f"The name of Solar panel is {self.name}\n"
                f"The origin country is {self.origin_country}\n"
                f"The producer is {self.producer}\n"
                f"The price is {self.price} hryvnia \n"
                f"The size in cm is {self.size_in_cm}\n"
                f"The power in watts is {self.power_in_watts}\n"
                f"The expiration date is {self.expiration_date}\n"
                f"The type of color of panel is {self.color_of_shining}\n"
                f"The capacity is {self.capacity} watts \n"
                f"The production or energy per day is {self.production_of_energy_per_day} watts \n")

    def get_capacity(self):
        return self.capacity

    def get_production_of_energy_per_day(self):
        return self.production_of_energy_per_day

    def set_capacity(self, capacity):
        self.capacity = capacity

    def set_production_of_energy_per_day(self, production_of_energy_per_day):
        self.production_of_energy_per_day = production_of_energy_per_day
