import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('成绩表.csv', encoding='UTF8')
df = df.fillna(method='backfill')
# print(df.to_string())
# print(df)
# print(df['姓名'], df['期末'])
newcol = df['平时'] * 0.1 + df['实验'] * 0.1 + df['期末'] * 0.7
# print(newcol)
# plt.bar(df.姓名, newcol)
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.scatter(df.姓名, newcol)
plt.show()
