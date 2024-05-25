from typing import List, Dict
from datetime import date, datetime

from address import Address
from audi import Audi
from movie import Movie
from show import Show

from enums import Genre

class CinemaHall:
    def __init__(self, cinema_hall_id: int, cinema_hall_name: str, address: Address):
        self.cinema_hall_id = cinema_hall_id
        self.cinema_hall_name = cinema_hall_name
        self.address = address
        self.audi_list: List[Audi] = []

    def get_movies(self, date_list: List[date]) -> Dict[date, List[Movie]]:
        # Placeholder implementation for get_movies
        return {date: [Movie("Sample Movie", 1, 120, "English", Genre.DRAMA, date)] for date in date_list}

    def get_shows(self, date_list: List[date]) -> Dict[date, List[Show]]:
        # Placeholder implementation for get_shows
        return {date: [Show(1, Movie("Sample Movie", 1, 120, "English", Genre.DRAMA, date), datetime.now(), datetime.now(), self)] for date in date_list}
