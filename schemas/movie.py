from dataclasses import dataclass


@dataclass
class MovieBase:
    title: str
    year: int
    type: str

    def __repr__(self) -> str:
        return (f"Movie(title={self.title!r}, year={self.year!r}, type={self.type!r})")


@dataclass
class MovieDetail(MovieBase):
    genre: str
    director: str
    imdbRating: float

    def __repr__(self) -> str:
        return (f"Movie(title={self.title!r}, year={self.year!r}, type={self.type!r}, "
                f"genre={self.genre!r}, director={self.director!r}, imdbRating={self.imdbRating!r})")
