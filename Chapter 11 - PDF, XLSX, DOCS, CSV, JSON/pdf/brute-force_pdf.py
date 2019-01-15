import PyPDF2, sys


words = open('dictionary.txt', 'r')

pdf_reader = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
for i in words:
    if pdf_reader.decrypt(i):
        print(i)
        break
    elif pdf_reader.decrypt(i):
        print(i.lower())
        break