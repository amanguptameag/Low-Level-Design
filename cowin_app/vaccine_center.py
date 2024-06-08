import uuid
from user import User
from slot import Slot

class VaccineCenter:
    def __init__(self, name, location):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.slots = {}

    def add_slot(self, time: str):
        if time not in self.slots:
            self.slots[time] = Slot(time)

    def book_slot(self, time: str, user: User):
        if time in self.slots:
            slot = self.slots[time]
            if slot.book(user):
                print("done")
            else:
                print("already booked")
        else:
                print("slot not available")