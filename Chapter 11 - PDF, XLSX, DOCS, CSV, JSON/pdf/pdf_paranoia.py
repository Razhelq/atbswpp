# pdf_paranoia.py - finds all pdf files in current working directory and encrypt them with provided password

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
            print(filename[:len(filename)-4])
            pdf_output = open('{}_encrypted.pdf'.format(filename[:len(filename)-4]), 'wb')
            pdf_writer.encrypt(pw)
            pdf_writer.write(pdf_output)
            pdf_output.close()
            pdf_file_obj.close()

for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('_encrypted.pdf'):
            if PyPDF2.PdfFileReader(open(os.path.join(os.getcwd() + '\\' + filename), 'rb')).isEncrypted:
                pdf_reader = PyPDF2.PdfFileReader(open(os.path.join(os.getcwd() + '\\' + filename), 'rb'))
                if pdf_reader.decrypt(pw):
                    os.remove(filename[:len(filename)-14] + '.pdf')

