import pytest

from pytemplate.domain.models import Movie


def test_valid_movie():
    movie = Movie(name="The Matrix", customer_age=18)
    assert movie.name == "The Matrix"
    assert movie.customer_age == 18


def test_invalid_age():
    with pytest.raises(ValueError) as e:
        Movie(name="The Matrix", customer_age=-1)
    assert str(e.value) == "Age must be a positive integer"


def test_invalid_age_type():
    with pytest.raises(ValueError) as e:
        Movie(name="The Matrix", customer_age="18")


def test_invalid_name_type():
    with pytest.raises(TypeError) as e:
        Movie(name=1, customer_age=18)
    assert str(e.value) == "Name must be a string"


def test_invalid_age_zero():
    with pytest.raises(ValueError) as e:
        Movie(name="The Matrix", customer_age=0)
    assert str(e.value) == "Age must be a positive integer"
