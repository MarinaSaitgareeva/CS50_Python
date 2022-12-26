from plates import is_valid


def main():
    test_is_valid_starts_with_two_letters()
    test_is_valid_number_of_characters()
    test_is_valid_ends_with_number()
    test_is_valid_first_number_not_zero()
    test_is_valid_punctuation()


def test_is_valid_starts_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("4422") == False


def test_is_valid_number_of_characters():
    assert is_valid("CS50") == True
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_is_valid_ends_with_number():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False


def test_is_valid_first_number_not_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_is_valid_punctuation():
    assert is_valid("CS50") == True
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    main()
