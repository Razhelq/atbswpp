import sys, PyPDF2, os

pw = sys.argv[1]

for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_file_obj = open(os.path.join(os.getcwd() + '\\' + filename), 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            for page_num in range(1, pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page_obj)
            pdf_output = open('{}_encrypted.pdf'.format(filename), 'wb')
            pdf_writer.encrypt(pw)
            pdf_writer.write(pdf_output)
            pdf_output.close()
