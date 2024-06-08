from user import User
from vaccine_center import VaccineCenter

class CowinApp:
    def __init__(self):
        self.users = {}
        self.centers = {}

    def register_user(self, name: str):
        user = User(name)
        self.users[user.id] = user
        return user.id
    
    def add_center(self, name: str, location: str):
        center = VaccineCenter(name, location)
        self.centers[center.id] = center
        return center.id
    
    def add_slot_to_center(self, center_id: str, time: str):
        if center_id in self.centers:
            center = self.centers[center_id]
            center.add_slot(time)

    def book_slot(self, user_id: str, center_id: str, time: str):
        if user_id in self.users:
            user = self.users[user_id]
            if center_id in self.centers:
                center = self.centers[center_id]
                center.book_slot(time, user)

    def view_centers(self):
        for center in self.centers.values():
            print(center.name)

    def view_users(self):
        for user in self.users.values():
            print(user.name)