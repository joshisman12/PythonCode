import pandas as pd

excel_file = '.\\TRA_山區工務邊坡區段活動性排序.xlsx'

df = pd.read_excel(excel_file)

def set_route_name(row):
    if str(row['No']).startswith('Neiwan'):
        return '內灣線'
    elif str(row['No']).startswith('Western_N'):
        return '縱貫線北段'
    elif str(row['No']).startswith('Shenao'):
        return '深澳線'
    elif str(row['No']).startswith('Pinxi'):
        return '平溪線'
    elif str(row['No']).startswith('Huadong'):
        return '花東線'
    elif str(row['No']).startswith('Southlinkline'):
        return '南迴線'
    elif str(row['No']).startswith('Northlinkline'):
        return '北迴線'
    elif str(row['No']).startswith('Yilan'):
        return '宜蘭線'
    elif str(row['No']).startswith('Chichi'):
        return '集集線'
    elif str(row['No']).startswith('Taichung'):
        return '臺中線'

df['路線名'] = df.apply(set_route_name, axis=1)

output_excel = 'output_excel.xlsx'
df.to_excel(output_excel, index=False)