import sys
import re
from datetime import date
import inflect


p = inflect.engine()


def main():
    date_of_birth = input("Date of Birth: ").strip()
    year, month, day = check_date(date_of_birth)
    date_of_birth = date(year, month, day)
    today = date.today()
    difference_in_minutes = (today - date_of_birth).days * 24 * 60
    words = p.number_to_words(difference_in_minutes, andword="").capitalize()
    print(f"{words} minutes")


def check_date(date_of_birth):
    if not date_of_birth:
        sys.exit("Missing date")

    try:
        year, month, day = map(int, date_of_birth.split("-"))
        date_of_birth = date(year, month, day)
    except Exception:
        sys.exit("Invalid date")

    return year, month, day


if __name__ == "__main__":
    main()
