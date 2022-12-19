import random


def main():
    level = get_level()
    user_score = 0

    for _ in range(0, 10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_sum = x + y
        user_sum = input(f"{x} + {y} = ").strip()

        if user_sum.isnumeric() and int(user_sum) == correct_sum:
            user_score += 1

        else:
            print("EEE")

            attempt = 1
            while attempt < 3:
                user_sum = input(f"{x} + {y} = ").strip()

                if user_sum.isnumeric() and int(user_sum) == correct_sum:
                    user_score += 1
                    break

                else:
                    print("EEE")
                    attempt += 1
                    continue

            print(f"{x} + {y} = {correct_sum}")

    print(f"Score: {user_score}")


def get_level():
    while True:
        try:
            level = input("Level: ").strip()

            if int(level) in [1, 2, 3]:
                return int(level)

        except ValueError:
            pass

        except EOFError:
            break


def generate_integer(level):
    try:
        match level:
            case 1:
                number = random.randint(0, 9)
            case 2:
                number = random.randint(10, 99)
            case 3:
                number = random.randint(100, 999)
            case _:
                raise ValueError

        return number

    except ValueError:
        get_level()


if __name__ == "__main__":
    main()
