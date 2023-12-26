from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

topics = pd.read_csv('topics.csv')

for index, pages in topics.iterrows():
    # Set Header
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=pages['Topic'], ln=1, align='L')
    pdf.line(10, 20, 200, 20)

    # Set Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=pages['Topic'], align='R')

    for i in range(pages['Pages'] - 1):
        pdf.add_page()

        # Set Footer
        pdf.ln(275)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=pages['Topic'], align='R')

pdf.output('output.pdf')
