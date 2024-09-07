import datetime
from utilities.general_utils import generate_id

class Bill:
    def __init__(self, user_id, total_amount, id = generate_id()):
        self.id = id
        self.user_id = user_id
        self.total_amount = total_amount
        self.date = datetime.datetime.now()
        self.is_paid = False
        self.payment_date = None

        def set_payment_date(self):
            self.payment_date = datetime.datetime.now()
            self.is_paid = True
               