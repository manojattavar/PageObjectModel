import xlrd


class XLSReader:
    def __init__(self, path):
        self.path = path
        self.readxls = xlrd.open_workbook(path)

    def getCellData(self, sheetname, rowIndex, colIndex):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.cell_value(rowIndex, colIndex)

    def getCellDatabyColname(self, sheetname, rowIndex, colname):
        sheet = self.readxls.sheet_by_name(sheetname)
        for cnum in range(0, self.getColumncount(sheetname)):
            extractedcolname = sheet.cell_value(0, cnum)
            if(extractedcolname==colname):
                celldata = sheet.cell_value(rowIndex, cnum)
                if(celldata!=''):
                    return celldata
                else:
                    return ''

    def checkemptycell(self, sheetname, rowIndex, colIndex):
        sheet = self.readxls.sheet_by_name(sheetname)
        celltype = sheet.cell_type(rowIndex, colIndex)
        if(celltype==xlrd.XL_CELL_EMPTY):
            return True
        else:
            return False

    def getRowcount(self, sheetname):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.nrows

    def getColumncount(self, sheetname):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.ncols