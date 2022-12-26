from fuel import convert, gauge
import pytest


def main():
    test_convert_x_more_than_y()
    test_convert_zero_division()
    test_convert_and_gauge_correct_input()
    test_convert_not_integer()


def test_convert_x_more_than_y():
    with pytest.raises(ValueError):
        convert("4/3")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_and_gauge_correct_input():
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("1/1") == 100 and gauge(100) == "F"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/100") == 1 and gauge(1) == "E"


def test_convert_not_integer():
    with pytest.raises(ValueError):
        convert("cat/cat")


if __name__ == "__main__":
    main()
