import re


def main():
    print(count(input("Text: ").strip()))


def count(s):
    ums = re.findall(r"\bum\b", s, re.IGNORECASE)
    if ums:
        return len(ums)
    else:
        return 0


if __name__ == "__main__":
    main()
