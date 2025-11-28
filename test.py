import pandas as pd
import numpy as np
import os

os.chdir(r"C:\Users\r-kajihara\Desktop")
df = pd.read_excel("test02.xlsx")

header = df.columns

# pd.DataFrameから所定のヘッダーの列を抜き出してpd.Seriesに
header_num = 1
df1 = df[header[header_num]]
#df1 = df.iloc[:,header_num]

# データを求める幅を決める
data_start_sec = 0
data_end_sec = 5
data_pitch = 2000
df1_time_range = df1[data_start_sec:data_end_sec*data_pitch+1]

# ０以上の値の平均値を求める
df1_positive = df1_time_range.where(df1_time_range >= 0, other=0)    # ０以下を０にして正の数を残す
df1_positive_no_zero = df1_positive[df1_positive != 0]    # ０の箇所を削除して詰める
df1_positive_mean = df1_positive_no_zero.mean()     # 平均値を求める
print(df1_positive_no_zero)


