def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            result = (int(x) / int(y)) * 100

            if result > 100:
                continue
            elif result >= 99:
                return print("F")
            elif result <= 1:
                return print("E")
            else:
                return print(f"{round(result)}%")

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
