from Bulb import Bulb
from Enums.TypeOfEnergyUse import TypeOfEnergyUse


class Lamp(Bulb):
    def __init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date,
                 type_of_appointment, type_of_material):
        Bulb.__init__(self, name, origin_country, producer, price, size_in_cm, power_in_watts, expiration_date)
        self.type_of_appointment = type_of_appointment
        self.type_of_material = type_of_material

    def __str__(self):
        return (f"The type of lamp is {TypeOfEnergyUse.ORDINARY}\n"
                f"The name of Lamp is {self.name}\n"
                f"The origin country is {self.origin_country}\n"
                f"The producer is {self.producer}\n"
                f"The price is {self.price} hryvnia \n"
                f"The size in cm is {self.size_in_cm}\n"
                f"The power in watts is {self.power_in_watts}\n"
                f"The expiration date is {self.expiration_date}\n"
                f"The type of appointment is {self.type_of_appointment}\n"
                f"The type of material is {self.type_of_material}\n")
