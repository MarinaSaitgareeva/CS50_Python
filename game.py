import random


def main():
    while True:
        level = input("Level: ").strip()

        if level.isnumeric() and int(level) > 0:
            number = random.randint(1, int(level))

            while True:
                guess = input("Guess: ").strip()

                if guess.isnumeric() and int(guess) > 0:
                    if int(guess) < number:
                        print("Too small!")
                    elif int(guess) > number:
                        print("Too large!")
                    else:
                        return print("Just right!")


if __name__ == "__main__":
    main()
