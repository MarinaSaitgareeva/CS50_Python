import sys


def main():
    check_command_line_arg()

    try:
        with open(sys.argv[1]) as file:
            number_of_lines = 0
            for line in file:
                if (not line.isspace()) and (not line.lstrip().startswith("#")):
                    number_of_lines += 1

        print(number_of_lines)

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_command_line_arg():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
