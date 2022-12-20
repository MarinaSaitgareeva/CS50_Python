import sys
import csv


def main():
    check_command_line_arg()

    try:
        students = []

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})

            # print(students)

        with open(sys.argv[2], "w") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def check_command_line_arg():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif (".csv" not in sys.argv[1]) and (".csv" not in sys.argv[2]):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
