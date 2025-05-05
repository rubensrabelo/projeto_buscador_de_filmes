from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    year: int
    genre: str
    director: str
    imdbRating: float
