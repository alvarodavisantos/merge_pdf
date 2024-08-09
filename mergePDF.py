import PyPDF2
import os

files = os.listdir('PDFs')

merge_files = PyPDF2.PdfMerger()

for file in files:
    if '.pdf' in file:
        merge_files.append(f"PDFs/{file}")

merge_files.write(f"PDFs unico/PDF.pdf")