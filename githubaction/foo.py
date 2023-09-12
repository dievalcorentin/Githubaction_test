i = 50


def foo(number: int | None) -> int:
    return number or 100


foo(number=100)
print(i)
