def main():
    user_input = input("Greeting: ").strip().lower()
    print(f"${value(user_input)}")


def value(greeting):
    greeting = greeting.strip().lower()

    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
