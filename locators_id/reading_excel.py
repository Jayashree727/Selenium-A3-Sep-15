import xlrd
from reading_excel import excel_read


 path = r'C:\Users\jayashree\PycharmProjects\selenium_training\training\candidates_info.xlsx'
def excel_read():
    workbook = xlrd.open_workbook(path)
    workbook = workbook.sheet_by_name('reg_data')
    rows = worksheet.get_rows()

    header = next(rows)
    reg = {}
    for ele in rows:
        reg[ele[0].value] = ele[1].value


    return reg