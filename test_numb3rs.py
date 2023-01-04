from numb3rs import validate


def main():
    test_validate_words()
    test_validate_format()
    test_validate_range()


def test_validate_words():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False


def test_validate_format():
    assert validate("1") == False
    assert validate("1.2") == False
    assert validate("1.2.3") == False
    assert validate("1:2:3:4") == False
    assert validate("1.2.3.4") == True


def test_validate_range():
    assert validate("280.280.280.280") == False
    assert validate("255.280.280.280") == False
    assert validate("255.255.280.280") == False
    assert validate("255.255.255.280") == False
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True


if __name__ == "__main__":
    main()
