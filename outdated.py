def main():
    while True:
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]

        try:
            date = input("Date: ").strip()
            if "/" in date:
                # Split date to month, day, year and convert them to integers.
                month, day, year = list(map(int, date.split("/")))

                if month <= 12 and day <= 31:
                    # :02d - add 0 before month and day
                    return print(f"{year}-{month:02d}-{day:02d}")

            else:
                date = date.capitalize()
                month, day, year = date.split(" ")

                if month in months and int(day[:-1]) <= 31 and day[-1] == ",":
                    month = months.index(month) + 1
                    return print(f"{int(year)}-{month:02d}-{int(day[:-1]):02d}")

        except ValueError:
            pass

        except EOFError:
            break


if __name__ == "__main__":
    main()
