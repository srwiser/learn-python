import xlrd
import pandas as pd

sheet_names = []
fp = ("/Users/swapnilrastogi/TrustedAdvisor-AWS.xls")
xl = pd.ExcelFile(fp)
for name in xl.sheet_names:
    data = pd.read_excel(fp,skiprows=10,sheet_name=name)
    print(data.shape)
    wb = xlrd.open_workbook(fp)
    sheet = wb.sheet_by_name(name)
    col_names = sheet.row_values(10)
    for i in col_names:
        col_values = pd.DataFrame(data, columns=[i])
        print(col_values)
