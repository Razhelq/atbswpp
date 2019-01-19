# excel_to_csv.py - Converts all excel files inside current working directory to csv files


import csv, openpyxl, os


for excel_file in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if excel_file.endswith('.xlsx'):
        wb = openpyxl.load_workbook(excel_file)

        for sheet_name in wb.get_sheet_names():
            # Loop through every sheet in the workbook.
            sheet = wb.get_sheet_by_name(sheet_name)

            csv_filename = os.path.basename(excel_file)[:-5] + '_' + sheet_name + '.csv'
            csv_file = open(csv_filename, 'w', newline='')
            csv_writer = csv.writer(csv_file)

            # Loop through every row in the sheet.
            for row_num in range(1, sheet.max_row + 1):
                row_data = []
                # Loop through each cell in the row.
                for col_num in range(1, sheet.max_column + 1):
                    # Append each cell's data to row_data.
                    row_data.append(sheet.cell(row=row_num, column=col_num).value)
                # Write the row_data list to the CSV file.
                csv_writer.writerow(row_data)
            csv_file.close()
