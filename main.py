from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

topics = pd.read_csv('topics.csv')

for index, pages in topics.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=pages['Topic'], ln=1, align='L',)
    pdf.line(10, 20, 200, 20)

    for i in range(pages['Pages'] - 1):
        pdf.add_page()


pdf.output('output.pdf')