from user import User

class Slot:
    def __init__(self, time):
        self.time = time
        self.is_available = True
        self.booked_by = None

    def book(self, user: User):
        if self.is_available:
            self.is_available = False
            self.booked_by = user
            user.booked_slots.append(self)
            return True
        return False
        