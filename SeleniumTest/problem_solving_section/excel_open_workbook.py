# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("C:\\Users\\amit_pc\\Downloads\\Cyntra\\MPOS _ Product_documets\\documetn_set1\\Enforce multiple - Explanation.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(0, 0))
