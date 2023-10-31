import PyPDF2
import sys

inputs = sys.argv[1:]

def merger_pdf(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

merger_pdf(inputs)

