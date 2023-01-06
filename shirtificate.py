from fpdf import FPDF


class PDF:
    def __init__(self, name):
        # By default, a FPDF document has a A4 format with
        # portrait orientation (orientation="portrait", format="A4").
        self._pdf = FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        # Setting font: helvetica bold 20.
        self._pdf.set_font("helvetica", size=40)
        # Printing title.
        self._pdf.cell(
            w=0, h=40, txt="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C"
        )
        # Adding image.
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        # Setting font: helvetica bold 20.
        self._pdf.set_font("helvetica", size=20)
        # Setting color: white.
        self._pdf.set_text_color(255, 255, 255)
        # Printing name + took CS50.
        self._pdf.multi_cell(
            w=0,
            h=-200,
            txt=f"{name} took CS50",
            new_x="LEFT",
            new_y="NEXT",
            align="C",
        )

    def save(self, name):
        self._pdf.output(name)


def main():
    name = input("Name: ").strip().title()
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
