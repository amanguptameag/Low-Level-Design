from typing import List

from movie import Movie
from show import Show
from search import Search
from booking import Booking
from address import Address

from enums import UserType

class User:
    def __init__(self, user_id: int, username: str, password: str, name: str, email: str, address: Address, user_type : UserType):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.address = address
        self.user_type = user_type

class Customer(User):
    def make_booking(self, booking: Booking) -> Booking:
        # Placeholder implementation for make_booking
        return booking

    def get_booking(self) -> List[Booking]:
        # Placeholder implementation for get_booking
        return []
    
class Admin(User):
    def add_movie(self, movie: Movie) -> bool:
        # Placeholder implementation for add_movie
        return True

    def add_show(self, show: Show) -> bool:
        # Placeholder implementation for add_show
        return True