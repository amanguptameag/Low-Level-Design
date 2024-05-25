from bms_service import BMSService
from cinema_hall import CinemaHall
from address import Address
from audi import Audi

# Example usage
address = Address(123456, "Main Street", "Springfield", "IL", "USA")
audi_list = [Audi(1, "Audi 1", 200), Audi(2, "Audi 2", 150)]
cinema_hall = CinemaHall(1, "Regal Cinemas", address)
cinema_hall.audi_list.extend(audi_list)

service = BMSService()
service.cinemas.append(cinema_hall)