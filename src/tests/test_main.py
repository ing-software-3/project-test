from src.main import sum, sub, mult, is_greater


def test_sum():
    assert sum(2, 5) == 7


def test_sub():
    assert sub(5, 2) == 1


def test_mult():
    assert mult(5, 5) == 25
