from abc import ABC


class Goods(ABC):

    def __init__(self, type_of_lamp, name, origin_country, producer, price, size_in_cm, power_in_watts,
                 expiration_date):
        self.type_of_lamp = type_of_lamp
        self.name = name
        self.origin_country = origin_country
        self.producer = producer
        self.price = price
        self.size_in_cm = size_in_cm
        self.power_in_watts = power_in_watts
        self.expiration_date = expiration_date
