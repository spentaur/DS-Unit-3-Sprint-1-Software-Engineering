from random import randint, sample, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Generate random Products

    Keyword Arguments:
        num_products {int} -- number of products to generate (default: {30})

    Returns:
        list -- a list of the randomly generated products
    """
    products = []
    for _ in range(num_products):
        name = f"{choice(ADJECTIVES)} {choice(NOUNS)}"
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):
    """Create a report from a list of Products"""
    prices_total = 0
    weights_total = 0
    flammability_total = 0
    product_names = set()
    num_of_products = len(products)

    for product in products:
        prices_total += product.price
        weights_total += product.weight
        flammability_total += product.flammability
        product_names.add(product.name)

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: ", len(product_names))
    print("Average price: ", prices_total / num_of_products)
    print("Average weight: ", weights_total / num_of_products)
    print("Average flammability: ", flammability_total / num_of_products)


if __name__ == '__main__':
    inventory_report(generate_products())
