import os
import xlrd
from xlutils.copy import copy
from common.all_path import Data_Path


class ExcelOperate:

    def __init__(self,fileName, sheet_index=0):

        self.book = xlrd.open_workbook(Data_Path+os.sep+fileName)
        self.sheet = self.book.sheet_by_index(sheet_index)
        self.fileName = fileName


    def read_excel(self):

        title = self.sheet.row_values(0)
        return [dict(zip(title,self.sheet.row_values(row))) for row in range(1, self.sheet.nrows)]

    def find_row_col_by_value(self, value):
        for row_idx in range(self.sheet.nrows):
            for col_idx in range(self.sheet.ncols):
                if self.sheet.cell_value(row_idx, col_idx) == value:
                    return row_idx, col_idx
        return None

    def update_excel(self,row, col, value):

        wb = copy(self.book)
        ws = wb.get_sheet("sheet1")
        ws.write(row, col+9, value)
        wb.save(Data_Path+os.sep+self.fileName)




if __name__ == '__main__':
    c,v = ExcelOperate("login_test.xls").find_row_col_by_value("case_1")
    print(c,v)
    ExcelOperate("login_test.xls").update_excel(c,v,"pass")



