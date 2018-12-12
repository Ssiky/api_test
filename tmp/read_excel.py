# 1.导入xrld
import xlrd

# 2.打开excel(work_book)
excel=xlrd.open_workbook("../data/data.xlsx")

# 3.指定工作表
sheet=excel.sheet_by_name("登录")
sheet=excel.sheet_by_index(0)

# 4.读取信息
print(sheet.nrows)  #有效数据行数
print(sheet.ncols)  #有效数据列数

print(sheet.row_values(0))    #打印第一行数据
print(sheet.row_values(0))    #打印第一行数据

print(sheet.cell(2,1).value)   #打印指定单元格数据

# 打印所有注册模块的用例（不要标题行）
sheet2=excel.sheet_by_name("注册")
for i in range(1,sheet2.nrows):
    print(sheet2.row_values(i))

