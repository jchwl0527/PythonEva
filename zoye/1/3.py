import matplotlib.pyplot as plt
import pandas as pd

path = r'/成绩单.xlsx'
frame = pd.read_excel(path)
print(frame.姓名)
print(frame.成绩)
plt.scatter(frame.姓名, frame.成绩)
plt.show()

import pandas as pd

df = pd.read_csv('chengji.csv', encoding='ansi')
print(df.to_string())
print(df)
print(df.姓名, df.卷面成绩)
newcol = df.平时成绩 * 0.1 + df.实验成绩 * 0.2 + df.卷面成绩 * 0.7
df2 = pd.DataFrame(newcol, index=["综合成绩"])
plt.scatter(df.姓名, newcol)
plt.plot(newcol)
plt.show()
