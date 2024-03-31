import pandas as pd

inp = r".\Excel轉GEO2010MDB.xlsx"
BasicInfo = pd.read_excel(inp, sheet_name='鑽孔基本資訊', header=2)
TestData = pd.read_excel(inp, sheet_name='試驗資料', header=2)
LithologyRecord = pd.read_excel(inp, sheet_name='地質圖元', header=2)

#merge1 = pd.concat([input_BasicInfo, input_TestData])

# 單獨取出不同資料來做成資料表
TestData_General = TestData.iloc[:, 0:22]
TestData_Shearing = TestData.iloc[:, 22:31]
TestData_Compression = TestData.iloc[:, 31:37]
TestData_RQD = TestData.iloc[:, 37:42]
LithologyRecord_Attr = LithologyRecord.iloc[:, 0:6]

# 刪除整列都是NaN值的列
TestData_General = TestData_General.dropna(axis=0, how='all')
TestData_Shearing = TestData_Shearing.dropna(axis=0, how='all')
TestData_Compression = TestData_Compression.dropna(axis=0, how='all')
TestData_RQD = TestData_RQD.dropna(axis=0, how='all')

# 更新SQL SERVER 資料表


#BasicInfo.to_csv(r'.\BoreholeBasicInfo.csv',encoding='utf-8-sig')
TestData_General.to_csv(r'.\BoreholeTestData_General.csv',encoding='utf-8-sig')
#TestData_Shearing.to_csv(r'.\BoreholeTestData_Shearing.csv',encoding='utf-8-sig')
#TestData_Compression.to_csv(r'.\BoreholeTestData_Compression.csv',encoding='utf-8-sig')
#TestData_RQD.to_csv(r'.\BoreholeTestData_RQD.csv',encoding='utf-8-sig')
#LithologyRecord_Attr.to_csv(r'.\BoreholeLithologyRecord_Attr.csv',encoding='utf-8-sig')


