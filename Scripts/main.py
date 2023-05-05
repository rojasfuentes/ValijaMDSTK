example =['DESTRUMPNOV',
'16004343',
'16004344',
'DE-23-001',
'REEN-16004344']

import pandas as pd

file_path = r'C:\Users\Mayo\Downloads\Valija\Archivos\Calidad de la orden (2).csv'
df = pd.read_csv(file_path)
df = df.iloc[:, [1, 2, 21, 24, 23, 33, 32]]

print(df.head())

""" init = 0
for i in df.keys():
    print(str(init) +' ' + i)
    init += 1 """
