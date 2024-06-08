# City -> Movies -> Theatre -> Audi -> Show -> Seat  -> Payment -> Booking -> User 

from datetime import date, datetime
from typing import List
from enum import Enum

class Genre(Enum):
    DRAMA = "DRAMA"
    SCI_FI = "SCI_FI"
    ACTION = "ACTION"
    HORROR = "HORROR"

class SeatType(Enum):
    DELUX = "DELUX"
    VIP = "VIP"

class SeatStatus(Enum):
    BOOKED = "BOOKED"
    AVAILABLE = "AVAILABLE"

class BookingStatus(Enum):
    CONFIRMED = "CONFIRMED"
    PENDING = "PENDING"

class PaymentStatus(Enum):
    CONFIRMED = "CONFIRMED"
    PENDING = "PENDING"


class BMSService:
    def __init__(self):
        self.theatres: List[Theatre] = []

    def get_movies(self, date: date, city: str) -> List[Movie]:
        return []
    
    def get_theatres(self, city: str) -> List[Theatre]:
        return []
    
class Theatre:
    def __init__(self, theatre_id: int, theatre_name: str, address: Address, audi_list: List[Audi]):
        self.theatre_id = theatre_id

    def get_movies(self, date: date) -> List[Movie]:
        return []
    
    def get_shows(self, date: date) -> List[Show]:
        return []
    
class Movie:
    def __init__(self, movie_id: int, movie_name: str, duration: int, release_date: date, genre: Genre, language: str):
        ''

class Address:
    def __inti__(self, street: str, city: str, state: str, country: str, pincode: int):
        ''

class Audi:
    def __init__(self, audi_id: int, audi_name: str, totol_seats: int, shows: List[Show]):
        ''

class Show:
    def __init__(self, show_id: int, movie: Movie, seats: List[Seat], start_time: datetime, end_time: datetime, theatre: Theatre):
        ''

class Seat:
    def __init__(self, seat_id: int, seat_type: SeatType, seat_status: SeatStatus, price: float):
        ''

class Booking:
    def __init__(self, booking_id: int, booking_date: date, show: Show, audi: Audi, seats: List[Seat], booking_status: BookingStatus, patment: Payment, user: User):
        ''

class Payment:
    def __init__(self, payment_id: int, payment_status: PaymentStatus, amount: float, payment_date: date, transaction_id: str):
        ''

class User:
    def __init__(self, user_id: int, name: str, username: str, password: str, email: str, user_type: UserType):
        ''

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