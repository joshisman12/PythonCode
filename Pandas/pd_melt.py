import pandas as pd

inp = r".\AISearchAll.csv"

df = pd.read_csv(inp, encoding='utf-8')

df_out = pd.melt(df, id_vars=['Id', 'Shape_Length', 'Shape_Area', 'RF_sus', 'XGB_sus', 'ANN', 'RailwayLine'], value_vars=['RF_range', 'XGB_range',  'ANN_range'], var_name='AIMethod', value_name='Range')

print(df_out)
def combine_range_value(row):
    if row['AIMethod'] == 'RF_range':
        return row['RF_sus']
    elif row['AIMethod'] == 'XGB_range':
        return row['XGB_sus']
    else:
        return row['ANN']

df_out1 = pd.DataFrame({
    'Id': df_out['Id'],
    'AIMethod': df_out['AIMethod'],
    'Range': df_out['Range'],
    'Range_Value': df_out.apply(combine_range_value, axis=1),
    'Shape_Length': df_out['Shape_Length'],
    'Shape_Area': df_out['Shape_Area'],
    'RailwayLine': df_out['RailwayLine'],
})

print(df_out1)
df_out1.to_csv(r'.\AISearchAllUnpivot.csv', encoding='utf-8-sig')