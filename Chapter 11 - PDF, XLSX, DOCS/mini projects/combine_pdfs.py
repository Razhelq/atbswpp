# combine_pdfs.py - Combines all the PDFs in the current working directory into a single PDF.


import PyPDF2, os


# Get all the PDF filenames.
pdf_files = []
for filename in os.listdir('..\\..\\automate_online-materials'):
    if filename.endswith('.pdf'):
        if not PyPDF2.PdfFileReader(open(os.path.join('..\\..\\automate_online-materials\\' + filename), 'rb')).isEncrypted:
            pdf_files.append(filename)

pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

# Loop trough all the PDF files.
for filename in pdf_files:
    pdf_file_obj = open(os.path.join('..\\..\\automate_online-materials\\' + filename), 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

pdf_output = open('allminutes.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()

