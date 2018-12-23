import numpy as np
import pandas as pd


dir_list=['化石翼龙','妙蛙花','水箭龟','皮卡丘']
for dir in dir_list:
    file_path = dir+'/Stat.csv'
    file=open(file_path)
    df=pd.read_csv(file)
    file.close()
    if not pd.isnull(df['Stat'][0]):
        continue

    df=df.iloc[1:7,0:2]
    df.columns=['Stat','Value']
    df['Stat'] = [x.strip(':') for x in df['Stat']]
    df['Value'] = [int(x) for x in df['Value']]
    df.to_csv(file_path,index=False)
