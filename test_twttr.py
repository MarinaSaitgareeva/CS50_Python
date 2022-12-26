from twttr import shorten


def main():
    test_shorten_lower_case()
    test_shorten_upper_case()
    test_shorten_number()


def test_shorten_lower_case():
    assert shorten("twitter") == "twttr"


def test_shorten_upper_case():
    assert shorten("WHAT'S YOUR NAME?") == "WHT'S YR NM?"


def test_shorten_number():
    assert shorten("CS50") == "CS50"


if __name__ == "__main__":
    main()
