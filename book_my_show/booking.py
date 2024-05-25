from typing import List, Optional
from datetime import date, datetime

from audi import Audi
from user import *
from show import Show
from payment import Payment
from seat import Seat

from enums import *

class Booking:
    def __init__(self, booking_id: str, booking_date: date, user: User, audi: Audi, show: Show, booking_status: BookingStatus, total_amount: float, payment_id: int):
        self.booking_id = booking_id
        self.booking_date = booking_date
        self.user = user
        self.audi = audi
        self.show = show
        self.booking_status = booking_status
        self.total_amount = total_amount
        self.payment_id: int = payment_id
        self.seats: List[Seat] = []
