class Bag:

    def __init__(self):
        self._reward = {}

    def put_all(self, item):
        for i in item:
            name = i['name']
            self._reward[name] = self._reward.get(name, 0) + i['value']

    def put(self, item):
        if type(item) is list:
            self.put_all(item)
        else:
            self.put_all([item])

    def get_all(self):
        return self._reward

    def get_quantity_by_name(self, name):
        return self._reward.get(name, 0)

    def take_quantity_from_item_by_name(self, name, quantity):
        if self.get_quantity_by_name(name) >= quantity:
            quantity = self._reward[name] = self._reward.get(name, 0) - quantity
        else:
            quantity = "No hay suficiente"
        return quantity