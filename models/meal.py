from utilities.general_utils import generate_id


class Meal:
    def __init__(self, name, price, id=generate_id()):
        self.id = id
        self.name = name
        self.price = price
