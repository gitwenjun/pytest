import os

import xlrd

from common.all_path import Data_Path


class ExcelOperate:

    def __init__(self,fileName,sheet_index = 0):
        self.book = xlrd.open_workbook(Data_Path+os.sep+fileName)
        self.sheet = self.book.sheet_by_index(sheet_index)

    def read_excel(self):
        title = self.sheet.row_values(0)
        return [dict(zip(title,self.sheet.row_values(row))) for row in range(1, self.sheet.nrows)]

    def write_excel(self):
        pass

