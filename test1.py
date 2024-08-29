# python function to read a excel file and return the data in a list of list format
def read_excel(file_path):
    import openpyxl
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))
    return
# nain function to test the read_excel function
if __name__ == '__main__':
    file_path = 'test.xlsx'
    data = read_excel(file_path)
    print(data)
