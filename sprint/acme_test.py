import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_and_explode(self):
        """Test product stealability and make it explode."""
        prod = Product('Test Product', 20, 30, 1)
        self.assertEqual(prod.stealability(), "Kinda stealable.")
        self.assertEqual(prod.explode(), "...boom!")

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""

    def test_default_num_products(self):
        """Test the default number of products"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        names = [product.name.split(" ") for product in generate_products]
        for adj, noun in names:
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
