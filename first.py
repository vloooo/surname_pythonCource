def add_numbers(x, y):
    return x + y


def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"
