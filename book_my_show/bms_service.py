from typing import List
from datetime import date

from movie import Movie
from cinema_hall import CinemaHall

class BMSService:
    def __init__(self):
        self.cinemas: List[CinemaHall] = []

    def get_movies(self, date: date, city: str) -> List[Movie]:
        movies = []
        for cinema in self.cinemas:
            if cinema.address.city == city:
                movies.extend(cinema.get_movies([date])[date])
        return movies

    def get_cinema_halls(self, city: str) -> List[CinemaHall]:
        return [cinema for cinema in self.cinemas if cinema.address.city == city]
