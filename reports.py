import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """ Creates a PDF file that contains data about the flatmate such as their names,their due amount and the period
    of the bill """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period Label and Value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert Name and Due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1pay, border=0, ln=1)

        # Insert Name and Due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2pay, border=0, ln=1)

        pdf.output(f"files/{self.filename}")

        os.chdir("files")  # change the directory to open PDF

        webbrowser.open(self.filename)