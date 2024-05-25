from typing import List

from show import Show

class Audi:
    def __init__(self, audi_id: int, audi_name: str, total_seats: int):
        self.audi_id = audi_id
        self.audi_name = audi_name
        self.total_seats = total_seats
        self.shows: List[Show] = []