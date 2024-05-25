from enums import *

class Seat:
    def __init__(self, seat_id: int, seat_type: SeatType, seat_status: SeatStatus, price: float):
        self.seat_id = seat_id
        self.seat_type = seat_type
        self.seat_status = seat_status
        self.price = price