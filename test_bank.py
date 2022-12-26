from bank import value


def main():
    test_value_start_with_hello()
    test_value_start_with_h()
    test_value_start_with_not_hello_or_h()


def test_value_start_with_hello():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("hello, Newman") == 0


def test_value_start_with_h():
    assert value("How you doing?") == 20
    assert value("hi!") == 20


def test_value_start_with_not_hello_or_h():
    assert value("What's happening?") == 100
    assert value("What's up?") == 100


if __name__ == "__main__":
    main()
