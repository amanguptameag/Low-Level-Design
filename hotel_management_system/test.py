# Actors: Guest, Receptionist, Admin, Server, HouseKeeping

# Use Cases:
# 1. Add/Remove/Edit Room
# 2. Search Room
# 3. Book Room
# 4. Cancel Room
# 5. Check In, Check Out
# 6. Add Room Charge
# 7. Update House Keeping log

from typing import List
from enum import Enum
from datetime import date

class RoomType(Enum):
    STANDARD = 'STANDARD',
    DELUX = 'DELUX'

class RoomStatus(Enum):
    BOOKED = 'BOOKED'
    AVAILABLE = 'AVAILABLE'

class AccountStatus(Enum):
    ACTIVE = 'ACTIVE'
    CLOSED = 'CLOSED'

class Hotel:
    def __init__(self,
                 id: int,
                 name: str,
                 address: Location,
                 room_list: List[Room]
                 ): ''

class Location:
    def __init__(self,
                 street: str,
                 city: str,
                 country: str,
                 pincode: int
                 ): ''

class Room:
    def __init__(self,
                 room_number: str,
                 room_type: RoomType,
                 room_status: RoomStatus,
                 price: float,
                 room_keys: List[RoomKey],
                 house_keeping_logs: List[HouseKeepingLog]
                 ): ''

class RoomKey:
    def __init__(self,
                 key_id: str,
                 bar_code: str,
                 issued_at: date,
                 is_active: bool,
                 is_master: bool
                 ): ''
    
    def assignRoom(self, room: Room) -> None: ''
    
class HouseKeepingLog:
    def __init__(self,
                 description: str,
                 date: date,
                 duration: int,
                 housekeeper: HouseKeeper
                 ): ''
    
    def add_room(self, room: Room) -> None: ''
    
class Person:
    def __init__(self,
                 name: str,
                 username: str,
                 password: str,
                 phone: str,
                 account_sattus: AccountStatus
                 ): ''
    
class HouseKeeper(Person):
    def get_room_serviced(self, date: date) -> List[Room]: ''

class Guest(Person):
    def __init__(self,
                 search_obj: SearchObj,
                 booking_obj: BookingObj
                 ): ''
    
    def get_all_room_bookings(self) -> List[RoomBooking]: ''

class Receptionist(Person):
    def __init__(self,
                 search_obj: SearchObj,
                 booking_obj: BookingObj
                 ): ''
    
    def check_in_guest(self, guest: Guest, booking_info: RoomBooking): ''
    def check_out_guest(self, guest: Guest, booking_info: RoomBooking): ''

class Admin(Person):
    def add_room(self, room: Room): ''
    def delete_room(self, room: Room): ''
    def edit_room(self, room: Room): ''
