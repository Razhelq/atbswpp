# pdf_decrypter -   finds every encrypted pdf file in current working directory
#                   and creates a decrypted copy using a provided password.


import PyPDF2, os, sys


for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfFileReader(open(os.path.join(os.getcwd() + '\\' + filename), 'rb'))
            if pdf_reader.isEncrypted:
                pdf_writer = PyPDF2.PdfFileWriter()
                try:
                    pdf_reader.decrypt(sys.argv[1])
                    for page_num in range(1, pdf_reader.numPages):
                        page_obj = pdf_reader.getPage(page_num)
                        pdf_writer.addPage(page_obj)
                except:
                    print('Password is incorrect')
                pdf_output = open(os.path.join(os.getcwd() + '\\' + filename[:len(filename)-14] + '.pdf'), 'wb')
                pdf_writer.write(pdf_output)
                pdf_output.close()
