from enum import Enum

class Genre(Enum):
    SCI_FI = "SCI_FI"
    DRAMA = "DRAMA"
    ROM_COM = "ROM_COM"
    FANTASY = "FANTASY"

class UserType(Enum):
    ADMIN = "ADMIN"
    GENERAL = "GENERAL"

class SeatType(Enum):
    DELUX = "DELUX"
    VIP = "VIP"
    ECONOMY = "ECONOMY"
    OTHER = "OTHER"

class SeatStatus(Enum):
    BOOKED = "BOOKED"
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    NOT_AVAILABLE = "NOT_AVAILABLE"

class BookingStatus(Enum):
    REQUESTED = "REQUESTED"
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

class PaymentStatus(Enum):
    UNPAID = "UNPAID"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    DECLINED = "DECLINED"
    CANCELLED = "CANCELLED"
    REFUNDED = "REFUNDED"