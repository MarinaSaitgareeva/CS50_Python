import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    check_command_line_arg()

    try:
        # Open an images
        image_before = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        # Get the width and height, respectively, of that image as a tuple.
        size = shirt.size
        # Resize version of the image to the requested output size in pixels,
        # , given as a (width, height) tuple.
        image_after = ImageOps.fit(image_before, size)
        # Overlay that image on top of another
        # the first shirt represents the image to overlay and
        # the second shirt represents a “mask” indicating which pixels in photo to update.
        image_after.paste(shirt, shirt)
        image_after.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_command_line_arg():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif (splitext(sys.argv[1].lower())[1] not in [".jpeg", ".jpg", ".png"]) and (
        splitext(sys.argv[2].lower())[1] not in [".jpeg", ".jpg", ".png"]
    ):
        sys.exit("Invalid output")
    elif splitext(sys.argv[1].lower())[1] != splitext(sys.argv[2].lower())[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
