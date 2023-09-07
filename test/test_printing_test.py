import pytest

from printing_test import hello_world


@pytest.mark.parametrize(
    "text, expected",
    [
        ('Corentin', "Hello world, Corentin"),
        ('Test', "Hello world, Test"),
        (None, "Hello world, welcome to Python test")
    ]
)
def test_hello_world(text, expected):
    assert hello_world(text) == expected
