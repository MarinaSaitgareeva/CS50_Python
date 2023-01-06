from jar import Jar
import pytest


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3
    with pytest.raises(ValueError) as erro_info:
        jar3 = Jar(-15)
    assert str(erro_info.value) == "Wrong capacity"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(2)
    assert jar.size == 7
    with pytest.raises(ValueError) as error_info:
        jar.deposit(10)
    assert str(error_info.value) == "Exceed capacity"


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(1)
    assert jar.size == 2
    with pytest.raises(ValueError) as error_info:
        jar.withdraw(10)
        assert str(error_info.value) == "Not enough cookies"


if __name__ == "__main__":
    main()
