import pandas as pd
from pandas.core.reshape.concat import concat

df1 = pd.read_csv('datasets/base_com_sentimentos.csv',sep=';',encoding='utf-8')
print(df1.head())

df2 = pd.read_csv('datasets/base_com_sentimentos - Copia.csv',sep=';',encoding='utf-8')
print(df2.head())

df3 = pd.concat([df1,df2])

df3.to_csv('datasets/base_com_sentimentos_df3.csv',sep=';',encoding='utf-8')