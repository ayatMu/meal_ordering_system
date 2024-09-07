from utilities.general_utils import generate_id


class Order:
    def __init__(self, bill_id, meal_id, quantity, price, id=generate_id()) -> None:
        self.id = id
        self.bill_id = bill_id
        self.meal_id = meal_id
        self.quantity = quantity
        self.price = price
