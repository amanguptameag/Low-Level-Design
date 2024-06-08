import uuid

class User:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.booked_slots = []

    def book_slot(self, slot):
        self.booked_slots.append(slot)
