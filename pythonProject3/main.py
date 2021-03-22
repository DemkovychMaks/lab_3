from Bulb import Bulb
from Garland import Garland
from Lamp import Lamp
from LED import LED
from LED_lamp import LedLamp
from Solar_panel import SolarPanel
from LightShopManager import LightShopManager
from Enums.TypeOfEnergyUse import TypeOfEnergyUse

a = Bulb("bulb", "china", "china", 24, 10, 100, 50)
b = Bulb("ordinary bulb", "Ukraine", "Maxus", 24, 6, 100, 320)
c = Lamp("modern lamp", "USA", "Philips", 1200, 30, 500, 600, "desktop", "plastic")
d = LED("LED", "Japan", "Lebron", 10, 1, 10, 700, "red")
e = LedLamp("modern LED lamp", "Canada", "Samsung", 1600, 50, 200, 365, "white", "day light")
f = Garland("X-Mas garland", "China", "ICICLE", 200, 300, 250, 120, "green", 250)
g = SolarPanel("Sun Shine", "German", "Solar Energy", 300, 3000, 300, 920, "green", 10000, 60)

all_objects = [a, b, c, d, e, f, g]
goods = LightShopManager(all_objects)


def sort_by_price_main():
    out = goods.sort_by_price(True)
    for i in out:
        print(i)
        print("--------------------")


def sort_by_power_main():
    out = goods.sort_by_power(True)
    for i in out:
        print(i)
        print("********************")


def find_by_type(type_of_lamp):
    out = goods.find_by_type(type_of_lamp)
    for i in out:
        print(i)
        print("####################")


sort_by_price_main()


sort_by_power_main()

find_by_type(TypeOfEnergyUse.ENERGYSAVING)
