class LightShopManager:
    def __init__(self, goods):
        self.goods = goods

    def sort_by_price(self, order):
        print("\n\nSorting by price\n")
        self.goods.sort(key=lambda x: x.price, reverse=order)
        out = self.goods
        return out

    def sort_by_power(self, order):
        print("\n\nSorting by power\n")
        self.goods.sort(key=lambda x: x.power_in_watts, reverse=order)
        out = self.goods
        return out

    def find_by_type(self, type_of_energy):
        out = list()
        print("\n\nFound by type: \n")
        for type_in_list in self.goods:
            if type_in_list.type_of_lamp == type_of_energy:
                out.append(type_in_list)
        return out
