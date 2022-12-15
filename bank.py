def bank():
    user_input = input("Greeting: ").strip().lower()
    all_words = user_input.split()
    first_word = all_words[0].replace(",", "")

    if user_input == "hello" or first_word == "hello":
        print("$0")
    elif user_input[0] == "h":
        print("$20")
    else:
        print("$100")


bank()
