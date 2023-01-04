from um import count


def main():
    test_word_with_um()
    test_uppercase_um()
    test_start_with_um()
    test_um_surronding_by_space()
    test_um_with_punctuation_marks()


def test_word_with_um():
    assert count("um thanks for the album") == 1


def test_uppercase_um():
    assert count("UM UM UM") == 3


def test_start_with_um():
    assert count("um") == 1
    assert count("um?") == 1


def test_um_surronding_by_space():
    assert count("My um car") == 1


def test_um_with_punctuation_marks():
    assert count("Um, thanks, um...") == 2


if __name__ == "__main__":
    main()
