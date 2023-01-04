import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    iframe = re.search(r"^<iframe .+></iframe>$", s, re.IGNORECASE)
    url = re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE)
    if iframe and url:
        return f"https://youtu.be/{url.group(1)}"


if __name__ == "__main__":
    main()
