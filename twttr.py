def main():
    user_input = input("Input: ")
    user_output = ""

    for letter in user_input:
        if letter.lower() not in ("a", "e", "i", "o", "u") and letter.upper() not in (
            "A",
            "E",
            "I",
            "O",
            "U",
        ):
            # print(letter, end="")
            user_output += letter

    print(f"Output: {user_output}")


if __name__ == "__main__":
    main()
