import re


def main():
    print(convert(input("hours: ").strip()))


def convert(s):
    working_time = re.search(
        r"^([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$",
        s,
    )

    if working_time:
        start_time = time_format(
            working_time.group(1), working_time.group(2), working_time.group(3)
        )
        end_time = time_format(
            working_time.group(4), working_time.group(5), working_time.group(6)
        )

        return f"{start_time} to {end_time}"

    else:
        raise ValueError


def time_format(hours, minutes, am_pm):
    if am_pm == "AM":
        if int(hours) == 12:
            hours = 0
        else:
            hours = int(hours)
    else:
        if int(hours) == 12:
            hours = 12
        else:
            hours = int(hours) + 12

    if minutes:
        minutes = minutes
    else:
        minutes = "00"

    return f"{hours:02}:{minutes}"


if __name__ == "__main__":
    main()
