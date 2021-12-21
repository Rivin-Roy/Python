#data visualisation
import pandas as pd
import matplotlib.pyplot as plot
df=pd.read_excel("D:\Python programs\canada.xls" ,sheet_name='Canada by Citizenship' ,skiprows=range(20) ,skipfooter=2)
print(df)
df=df.drop(columns=['Type','Coverage','AREA','AreaName','REG','RegName','DEV','DevName'])
print(df)
df=df.set_index('OdName')
print(df)
