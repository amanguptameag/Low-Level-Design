from datetime import date

from enums import *

class Payment:
    def __init__(self, payment_id: int, amount: float, payment_date: date, transaction_id: int, payment_status: PaymentStatus):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_date = payment_date
        self.transaction_id = transaction_id
        self.payment_status = payment_status