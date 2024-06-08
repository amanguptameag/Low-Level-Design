from enum import Enum
from datetime import date
from typing import List

class RoomStyle(Enum):
    STANDARD = "Standard"
    DELUXE = "Deluxe"
    FAMILY_SUITE = "Family Suite"

class RoomStatus(Enum):
    AVAILABLE = "Available"
    RESERVED = "Reserved"
    NOT_AVAILABLE = "Not Available"
    OCCUPIED = "Occupied"
    SERVICE_IN_PROGRESS = "Service in Progress"

class AccountStatus(Enum):
    ACTIVE = "Active"
    CLOSED = "Closed"
    BLOCKED = "Blocked"

class Location:
    def __init__(self, longitude: float, latitude: float):
        self.longitude = longitude
        self.latitude = latitude

class RoomKey:
    def __init__(self, key_id: str, bar_code: str, issued_at: date, is_active: bool, is_master: bool):
        self.key_id = key_id
        self.bar_code = bar_code
        self.issued_at = issued_at
        self.is_active = is_active
        self.is_master = is_master
        self.room = None

    def assign_room(self, room):
        self.room = room

class HouseKeeper:
    def __init__(self, name: str, account_detail, phone: str):
        self.name = name
        self.account_detail = account_detail
        self.phone = phone

class HouseKeepingLog:
    def __init__(self, description: str, start_date: date, duration: int, housekeeper: HouseKeeper):
        self.description = description
        self.start_date = start_date
        self.duration = duration
        self.housekeeper = housekeeper
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

class Room:
    def __init__(self, room_number: str, room_style: RoomStyle, room_status: RoomStatus, booking_price: float):
        self.room_number = room_number
        self.room_style = room_style
        self.room_status = room_status
        self.booking_price = booking_price
        self.room_keys = []
        self.housekeeping_logs = []

class Account:
    def __init__(self, username: str, password: str, account_status: AccountStatus):
        self.username = username
        self.password = password
        self.account_status = account_status

class Person:
    def __init__(self, name: str, account_detail: Account, phone: str):
        self.name = name
        self.account_detail = account_detail
        self.phone = phone

class Guest(Person):
    def __init__(self, name: str, account_detail: Account, phone: str):
        super().__init__(name, account_detail, phone)
        self.search_obj = Search()
        self.booking_obj = Booking()

    def get_all_room_bookings(self):
        # Logic to get all room bookings
        pass

    def create_booking(self):
        # Logic to create booking
        pass

    def cancel_booking(self, booking_id: int):
        # Logic to cancel booking
        pass

class Receptionist(Person):
    def __init__(self, name: str, account_detail: Account, phone: str):
        super().__init__(name, account_detail, phone)
        self.search_obj = Search()
        self.booking_obj = Booking()

    def check_in_guest(self, guest: Guest, booking_info):
        # Logic to check in guest
        pass

    def check_out_guest(self, guest: Guest, booking_info):
        # Logic to check out guest
        pass

class Admin(Person):
    def __init__(self, name: str, account_detail: Account, phone: str):
        super().__init__(name, account_detail, phone)

    def add_room(self, room_detail: Room):
        # Logic to add room
        pass

    def delete_room(self, room_id: str):
        # Logic to delete room
        pass

    def edit_room(self, room_detail: Room):
        # Logic to edit room
        pass

class Search:
    def search_room(self, room_style: RoomStyle, start_date: date, duration: int) -> List[Room]:
        # Logic to search room
        pass

class RoomBooking:
    def __init__(self, booking_id: str, start_date: date, duration_in_days: int, booking_status, guest_list: List[Guest], room_info: List[Room], total_room_charges):
        self.booking_id = booking_id
        self.start_date = start_date
        self.duration_in_days = duration_in_days
        self.booking_status = booking_status
        self.guest_list = guest_list
        self.room_info = room_info
        self.total_room_charges = total_room_charges

class BaseRoomCharge:
    def get_cost(self) -> float:
        raise NotImplementedError

class RoomCharge(BaseRoomCharge):
    def __init__(self, cost: float):
        self.cost = cost

    def get_cost(self) -> float:
        return self.cost

class RoomServiceCharge(BaseRoomCharge):
    def __init__(self, cost: float, base_room_charge: BaseRoomCharge):
        self.cost = cost
        self.base_room_charge = base_room_charge

    def get_cost(self) -> float:
        return self.base_room_charge.get_cost() + self.cost

class InRoomPurchaseCharges(BaseRoomCharge):
    def __init__(self, cost: float, base_room_charge: BaseRoomCharge):
        self.cost = cost
        self.base_room_charge = base_room_charge

    def get_cost(self) -> float:
        return self.base_room_charge.get_cost() + self.cost

class Booking:
    def create_booking(self, guest_info: Guest) -> RoomBooking:
        # Logic to create booking
        pass

    def cancel_booking(self, booking_id: int) -> RoomBooking:
        # Logic to cancel booking
        pass

class Hotel:
    def __init__(self, name: str, hotel_id: int, hotel_location: Location, room_list: List[Room]):
        self.name = name
        self.hotel_id = hotel_id
        self.hotel_location = hotel_location
        self.room_list = room_list
