import csv

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('成绩表.xlsx')
df.to_csv('csv1.csv', index=False)

with open('csv1.csv', mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    header_list = ["姓名", "总分", "平均分"]
    for row in reader:
        All = int(row[1]) + int(row[2]) + int(row[3])
        data_list = [str(row[0]), [All], [All / 3]]

        # print(row[0], data_list)

        j = open("new_data.csv", mode="a+", encoding="utf-8", newline="")
        j.writelines(str(data_list))

with open("new_data.csv", mode="a+", encoding="utf-8", newline="") as j:
    writer = csv.writer(j)
    writer.writerow(header_list)
    writer.writerows(data_list)

print("{}  {}: {}={}, {}={}, {}={}".format(header[0], row[0],
                                           header[1], row[1],
                                           header[2], row[2],
                                           header[3], row[3]))

# 生成图表
a = int(row[1])
b = int(row[2])
c = int(row[3])
d = str(header[1])
e = str(header[2])
f = str(header[3])
x = [d, e, f]
y = [a, b, c]
plt.bar(x, y)
plt.title(row[0])
plt.show()
