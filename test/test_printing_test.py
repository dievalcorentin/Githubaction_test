import pytest

import printing_test


@pytest.mark.parametrize(
    "text, expected",
    [
        ('Corentin', "Hello world, Corentin"),
        ('Test', "Hello world, Test"),
        (None, "Hello world, welcome to Python test")
    ]
)
def test_hello_world(text, expected):
    assert printing_test.hello_world(text) == expected
