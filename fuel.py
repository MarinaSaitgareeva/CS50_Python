def main():
    fraction = convert(input("Fraction: "))
    result = gauge(fraction)
    print(result)


def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            result = round(x / y * 100)

            if result <= 100:
                return result
            else:
                raise ValueError

        except (ValueError, ZeroDivisionError):
            raise
            # fraction = input("Fraction: ")
            # pass


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
