def playback():
    user_input = input("Please type some text here: ")
    print("Whitespaces in your text were converted to ... (three periods): ", end="")
    print(user_input.replace(" ", "..."))


playback()
