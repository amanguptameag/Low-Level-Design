from typing import List, Dict
from datetime import date

from show import Show

from enums import *

class Movie:
    def __init__(self, movie_name: str, movie_id: int, duration_in_mins: int, language: str, genre: Genre, release_date: date):
        self.movie_name = movie_name
        self.movie_id = movie_id
        self.duration_in_mins = duration_in_mins
        self.language = language
        self.genre = genre
        self.release_date = release_date
        self.city_show_map: Dict[str, List['Show']] = {}