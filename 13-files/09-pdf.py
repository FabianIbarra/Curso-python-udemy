import os
os.system("cls" if os.name == "nt" else "clear")

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="¡Hola mundo en PDF!", ln=True, align='C')
pdf.cell(200, 10, txt="PDF generado con Python", ln=True, align='C')
pdf.output("archivo_pdf.pdf")