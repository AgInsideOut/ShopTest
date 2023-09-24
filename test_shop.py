""" Write unit tests for your Simple Shop Program in Task 3.
You may need to refactor your function in Task 3 to 'untangle' some logic into smaller blocks of code to make it easier to write tests.
Write at least 5 unit tests in total covering various and appropriate cases. 
An expected test will see your custom error being raised. """

import unittest
import shop  # Import the shop module


class TestMyFunction(unittest.TestCase):
    def test_purchase_desire(self):
        request = "2"
        expected_output = "I see that you want to leave, have a wonderful day then!"
        self.assertNotEqual(shop.check_place_order(request), expected_output)

    def test_insufficient_funds(self):
        item_price = 20.99
        customer_budget = 100
        expected_output = "Sorry, the sum is not enough to buy the item."
        self.assertNotEqual(shop.check_funds(item_price, customer_budget), expected_output)

    def test_invalid_item(self):
        item_id = 8
        expected_output = "Sorry, the item you're looking for is unavailable."
        self.assertNotEqual(shop.check_item_availability(item_id), expected_output)

    def test_maximum_attempts_reached(self):
        attempts = 2
        max_attempts = 3
        expected_output = "Maximum attempts reached. Sorry, you need to leave."
        self.assertNotEqual(shop.check_attempts(attempts, max_attempts), expected_output)

    def test_additional_funds(self):
        attempts = 1
        max_attempts = 3
        item_price = 20.99
        customer_budget = 100
        self.assertTrue(shop.check_add_funds(attempts, max_attempts, item_price, customer_budget))
        
if __name__ == '__main__':
    unittest.main()
