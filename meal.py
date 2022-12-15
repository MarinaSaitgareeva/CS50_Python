def main():
    time = input("What time is it? ").strip().lower()
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    if len(time.split(" ")) < 2:
        hours, minutes = time.split(":")
        converted_time = float(hours) + float(minutes) / 60
        return round(converted_time, 2)

    else:
        time = time.replace(" ", ":")
        hours, minutes, am_pm = time.split(":")

        if am_pm == "p.m." and int(hours) != 12:
            converted_time = float(hours) + 12 + float(minutes) / 60
            return round(converted_time, 2)
        elif int(hours) == 12 and am_pm == "p.m.":
            converted_time = float(hours) + float(minutes) / 60
            return round(converted_time, 2)
        elif int(hours) == 12 and am_pm == "a.m.":
            converted_time = float(hours) + 12 + float(minutes) / 60
            return round(converted_time, 2)
        else:
            converted_time = float(hours) + float(minutes) / 60
            return round(converted_time, 2)


if __name__ == "__main__":
    main()
