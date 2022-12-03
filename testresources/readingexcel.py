from testresources import constants
from testresources.readdata import XLSReader


def getcelldata(testcasename, path):
    datalist = []
    xls = XLSReader(path)

    teststartrowindex = 0
    while not(xls.getCellData(constants.DATASHEET, teststartrowindex, 0) == testcasename):
        teststartrowindex = teststartrowindex+1

    colstartrowindex = teststartrowindex + 1
    datastartrowindex = teststartrowindex + 2

    maxrow = 0
    try:
        while not(xls.checkemptycell(constants.DATASHEET, datastartrowindex+maxrow, 0)):
            maxrow = maxrow+1
    except IndexError:
        pass

    maxcol = 0
    try:
        while not (xls.checkemptycell(constants.DATASHEET, colstartrowindex, maxcol)):
            maxcol = maxcol + 1
    except IndexError:
        pass

    for rNum in range(datastartrowindex, datastartrowindex+maxrow):
        datadictionary = {}
        for cNum in range(0, maxcol):
            datakey = xls.getCellData(constants.DATASHEET, colstartrowindex, cNum)
            datavalue = xls.getCellData(constants.DATASHEET, rNum, cNum)
            datadictionary[datakey] = datavalue
        datalist.append(datadictionary)
    return datalist


def isrunnable(testcasename, path):
    xls = XLSReader(path)
    rows = xls.getRowcount(constants.TESTSHEET)
    for rNum in range(0, rows):
        tname = xls.getCellDatabyColname(constants.TESTSHEET, rNum, constants.TCID)
        if tname == testcasename:
            runmode = xls.getCellDatabyColname(constants.TESTSHEET, rNum, constants.RUNMODE)
            if runmode == constants.RUNMODE_Y:
                return True
            else:
                return False
