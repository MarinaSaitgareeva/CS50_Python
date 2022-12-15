def faces():
    user_input = input("Please type some text (you can add smiles in it: \":)\" or \":(\") here: ")
    print("Your smiles in text were converted to images (🙂 or 🙁): ", end="")
    print(user_input.replace(":)", "🙂").replace(":(", "🙁"))


faces()
