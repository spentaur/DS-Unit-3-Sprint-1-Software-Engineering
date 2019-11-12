from random import randint


class Product:
    """One of the many goods sold by the Acme Corp."""

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """
        Determines how steable an Product is based on it's price / weight
        ratio.

        Returns:
            string -- how stealable a Product is.
        """
        price_weight_ratio = self.price / self.weight

        if price_weight_ratio < 0.5:
            return "Not so stealable..."
        elif 0.5 <= price_weight_ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Explodes the Product.

        Returns:
            string -- explosion level
        """

        flammability_time_weight = self.flammability * self.weight

        if flammability_time_weight < 10:
            return "...fizzle"
        elif 10 <= flammability_time_weight < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """A Boxing Glove is a type of Product."""

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        """
        Override Product explode method since this is a boxing glove
        and therefore has a very low explosive potential, almost
        negligible really.

        Returns:
            string -- it's a glove...
        """
        return "...it's a glove"

    def punch(self):
        """
        Hit someone with the glove, and get their reaction based on the
        weight of the glove.

        Returns:
            string -- victims reaction
        """
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
