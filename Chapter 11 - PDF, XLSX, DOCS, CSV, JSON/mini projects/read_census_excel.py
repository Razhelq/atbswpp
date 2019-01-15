# read_census_excel.py - Tabulates population and number of census tracts for each country.


import openpyxl, pprint


print('Opening workbook...')
wb = openpyxl.load_workbook('..\\..\\automate_online-materials\\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
country_data = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state   = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop     = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    country_data.setdefault(state, {})
    # Make sure the key for this country in this state exists.
    country_data[state].setdefault(country, {'tracts': 0, 'pop': 0})

    # Each row represents on census tract, so increment by one.
    country_data[state][country]['tracts'] += 1
    # Increase the country pop by the pop in this census tract.
    country_data[state][country]['pop'] += int(pop)

# Opens a new text file and write the contents of country_data to it.
print('Writing results...')
result_file = open('census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(country_data))
result_file.close()
print('Done.')




