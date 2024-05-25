from typing import List
from datetime import datetime

from cinema_hall import CinemaHall
from seat import Seat
from movie import Movie

class Show:
    def __init__(self, show_id: int, movie: Movie, start_time: datetime, end_time: datetime, cinema_played_at: 'CinemaHall'):
        self.show_id = show_id
        self.movie = movie
        self.start_time = start_time
        self.end_time = end_time
        self.cinema_played_at = cinema_played_at
        self.seats: List['Seat'] = []
