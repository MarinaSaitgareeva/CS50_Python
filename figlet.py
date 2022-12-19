import sys
from pyfiglet import Figlet
from random import choice


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = choice(fonts)
        figlet.setFont(font=font)
        user_input = input("Input: ").strip()
        print(f"Output: \n {figlet.renderText(user_input)}")

    elif len(sys.argv) == 3 and sys.argv[1] == "-f" and sys.argv[2] in fonts:
        font = sys.argv[2]
        figlet.setFont(font=font)
        user_input = input("Input: ").strip()
        print(f"Output: \n {figlet.renderText(user_input)}")

    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
