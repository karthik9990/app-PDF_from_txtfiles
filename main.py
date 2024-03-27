import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


fiepaths = glob.glob("Files/*.txt")

pdf = FPDF(orientation="P", format="A4",unit="mm")
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in fiepaths:
    pdf.add_page()

    filename = Path(filepath).stem
    name = filename.title()

    pdf.set_font(family="Arial", style="B", size=20)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=50, h=8, txt=name, ln=1)

    # get the description of text file
    with open(filepath, "r") as file:
        content = file.read()
        pdf.set_font(family="Arial", size=15)
        pdf.multi_cell(w=0, h=6, txt=content)


pdf.output("output.pdf")
