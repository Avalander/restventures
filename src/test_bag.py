import unittest
from bag import Bag

class TestBag(unittest.TestCase):
    def test_put_adds_item_to_inventory(self):
        bag = Bag()
        item = {'name':'piedra','value': 30}

        bag.put(item)

        self.assertEqual({'piedra': 30}, bag.get_all())

    def test_put_adds_multiple_items_to_inventory(self):
        bag = Bag()
        item = [{'name':'piedra','value': 30},{'name':'palo','value': 20}]

        bag.put(item)

        self.assertEqual({'piedra': 30, 'palo': 20}, bag.get_all())

    def test_put_sums_when_value_is_the_same(self):
        bag = Bag()

        item = [{'name': 'piedra', 'value': 30}, {'name': 'palo', 'value': 20},{'name': 'piedra', 'value': 15}]

        bag.put(item)

        self.assertEqual({'piedra': 45, 'palo': 20}, bag.get_all())

    def test_get_all_returns_all_items_in_bag(self):
        bag = Bag()

        item = [{'name':'piedra','value':1}, {'name':'palo','value':2},{'name':'libro','value':3}]

        bag.put(item)

        self.assertEqual({'piedra' : 1, 'palo' : 2, 'libro' : 3}, bag.get_all())


    #def test_put_raises_exception_when_bag_is_full(self):
    #    bag = Bag()
    #    item = {'value': 30}

    #   [bag.put(item) for _ in range(0, MAX_ITEMS)]

    #    self.assertRaises(ValueError, bag.put, [item])

    def test_get_quantity_by_name_returns_element(self):
        bag = Bag()

        item = [{'name': 'piedra', 'value': 1}, {'name': 'palo', 'value': 2}, {'name': 'libro', 'value': 3}]

        bag.put(item)

        actual = bag.get_quantity_by_name('piedra')
        self.assertEqual(1, actual)

    def test_get_quantity_by_name_returns_zero_when_nokey(self):
        bag = Bag()

        item = [{'name': 'piedra', 'value': 1}, {'name': 'palo', 'value': 2}, {'name': 'libro', 'value': 3}]

        bag.put(item)

        actual = bag.get_quantity_by_name('pedrusco')
        self.assertEqual(0, actual)

    def test_take_quantity_from_item_by_name_takes_the_quantity(self):
        bag = Bag()

        item = [{'name': 'piedra', 'value': 1}, {'name': 'palo', 'value': 2}, {'name': 'libro', 'value': 3}]

        bag.put(item)

        actual = bag.take_quantity_from_item_by_name('piedra', 1)

        self.assertEqual(0, actual)

    def test_take_quantity_from_item_by_name_controls_quantity(self):
        bag = Bag()

        item = [{'name': 'piedra', 'value': 1}, {'name': 'palo', 'value': 2}, {'name': 'libro', 'value': 3}]

        bag.put(item)

        actual = bag.take_quantity_from_item_by_name('piedra',2)

        self.assertEqual("No hay suficiente", actual)

    def test_take_quantity_from_item_by_name_controls_exxistence(self):
        bag = Bag()

        item = [{'name': 'piedra', 'value': 1}, {'name': 'palo', 'value': 2}, {'name': 'libro', 'value': 3}]

        bag.put(item)

        actual = bag.take_quantity_from_item_by_name('pedrusco',2)

        self.assertEqual("No hay suficiente", actual)
    
    def test_get_all_should_not_allow_to_modify_bags_reward(self):
        bag = Bag()

        item = {'name': 'cheese', 'value': 1}

        bag.put(item)
        data = bag.get_all()
        data['cheese'] = 4
        actual = bag.get_all()

        self.assertEqual({'cheese': 1}, actual)


if __name__ == '__main__':
    unittest.main()
