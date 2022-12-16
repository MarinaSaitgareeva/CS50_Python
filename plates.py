def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_two_letters = s[0:2]
    plate_wo_letters = [letter for letter in s if letter.isnumeric()]

    # All vanity plates must start with at least two letters
    if not first_two_letters.isalpha():
        return False
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    elif len(s) < 2 or len(s) > 6:
        return False
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    elif len(plate_wo_letters) != 0 and not s.endswith(
        "".join(str(e) for e in plate_wo_letters)
    ):
        return False
    # The first number used cannot be a ‘0’.
    elif len(plate_wo_letters) != 0 and plate_wo_letters[0] == "0":
        return False
    # No periods, spaces, or punctuation marks are allowed.
    elif not s.isalnum():
        return False
    else:
        return True


main()
