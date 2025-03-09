from dataclasses import dataclass


@dataclass
class Movie:
    name: str
    customer_age: int

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError("Name must be a string")

        if not isinstance(self.customer_age, int) or self.customer_age <= 0:
            raise ValueError("Age must be a positive integer")


def movie_factory(name: str, customer_age: int) -> Movie:
    return Movie(name=name, customer_age=customer_age)
