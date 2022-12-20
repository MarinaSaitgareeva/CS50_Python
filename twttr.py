def main():
    user_input = input("Input: ")
    user_output = shorten(user_input)

    print(f"Output: {user_output}")


def shorten(word):
    user_output = ""

    for letter in word:
        if letter.lower() not in ("a", "e", "i", "o", "u"):
            user_output += letter

    return user_output


if __name__ == "__main__":
    main()
