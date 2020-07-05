import xlrd
import json

sheet = xlrd.open_workbook('test.xlsx').sheet_by_index(0)

for i in range(1, sheet.nrows):
    print(json.loads(sheet.row_values(i)[2][13:]))
