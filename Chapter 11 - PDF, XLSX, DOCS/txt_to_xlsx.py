import openpyxl, os


wb = openpyxl.Workbook()
sheet = wb.active
count = 1

for foldername, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith('.txt'):
            r = 1
            file = open(os.path.join(os.path.abspath('.'), filename))
            for line in (file.readlines()):
                sheet.cell(row=r, column=count).value = line
                r += 1
            count += 1

wb.save('txt_to_xlsx.xlsx')