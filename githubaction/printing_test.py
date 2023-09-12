"""Printing test module"""

from datetime import datetime


def hello_world(text: str) -> str:
    """
    Creation of a hello world function
    :param text: What you want to add next to a hello world message
    :type text: str
    :return: Hello world message
    """
    if text:
        return f'Hello world, {text}'
    return 'Hello world, welcome to Python test'


date = datetime.now()
print(date)
print(type(date))

print("Nous sommes le:", datetime.now())
print(f"Nous sommes le: {datetime.now()}")
