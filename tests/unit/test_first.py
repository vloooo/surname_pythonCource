from first import add_numbers, factorial, is_even_or_odd


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_is_even_or_odd():
    assert is_even_or_odd(4) == "Even"
    assert is_even_or_odd(7) == "Odd"
    assert is_even_or_odd(0) == "Even"
    assert is_even_or_odd(-3) == "Odd"
