import PyPDF2
import sys
import os

# Initialize a PdfFileMerger object from PyPDF2 library
merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("Combined.pdf")
