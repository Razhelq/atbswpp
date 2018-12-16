# combine_pdfs.py - Combines all the PDFs in the current working directory into a single PDF.


import PyPDF2, os


# Get all the PDF filenames.
pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename

pdf_files.sort(key=str.lower())

pdf_writer = PyPDF2.PdfFileWriter()

# Loop trough all the PDF files.
for filename in pdf_files:
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)


