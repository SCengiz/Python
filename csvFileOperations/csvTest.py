# ... Created by Soray Cengiz - 01.05.2022 
import csv
import sys

# @class(csvClass) : A class that has been setup for the csv File csvFileOperations
# ... Here the class holds the file path information and the file rows.
class csvClass:
# @function(__init__): Constructor for csvClass
  def __init__(self, filePath):
    self.filePath = filePath
    self.rowList = []

# @function(takeRows): The function that take the rows of the csv input file.
# NOTE: This function called from readCsvFiles function.
  def takeRows(self, inCsvReader):
    for row in inCsvReader:
      self.rowList.append(row)

# @function(readCsvFiles): Function that open the file and called the takeRows functionn.
  def readCsvFiles(self):
    with open(self.filePath) as csvFile:
      csvReader = csv.reader(csvFile, delimiter=',')
      self.takeRows(csvReader)

# @function(removeLines) : Function that is removes the specified lines from the rowList parammeter.
  def removeLines(self, inputArg):
    for i in reversed(range(inputArg)): 
      self.rowList.pop(i)

# @function(createNewCsv) : This function creates a new file using new rowList parameter.      
  def createNewCsv(self):
    with open('output.csv', mode = 'w', newline='') as csvFile:
      write = csv.writer(csvFile)
      write.writerows(self.rowList)

# NOTE: filePath stores the your path of the csv file.
# NOTE: User needs to change this parameter.
filePath = r'C:\Users\soray\Desktop\csvFileOperations\input.csv'

takeInputDatas = csvClass(filePath)
takeInputDatas.readCsvFiles()

# NOTE: Lines up to this parameter that we want to delete in the csv input file.
inputArg = int(sys.argv[1])

takeInputDatas.removeLines(inputArg)
takeInputDatas.createNewCsv()
