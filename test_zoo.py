import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_child_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(1), 50)

    def test_teens_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)
    
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(100), 100)

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-10), "error")

    def test_bva(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_bva2(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_bva3(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)



        
if __name__ == '__main__':
    unittest.main()