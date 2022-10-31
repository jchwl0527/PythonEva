# import pandas as pd
#
# df = pd.read_csv('44.csv')
# print(df.to_string())

# while :
#     a1 = open("44.csv", 'r').readline()
#     print(a1)

# a2 = open("44.csv", 'w')
# num = a2.write("Syr,12,21,23,32,\n11,12,13")
# print(num)
# a2.close()
# Open file
import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fileHandler = open("1/1.csv", mode='r', encoding='utf8', )
# 获取文件中所有行的列表
listOfLines = fileHandler.readlines()
# 关闭文件
fileHandler.close()
# Iterate over the lines

for line in listOfLines:
    array = line.split(",")
    name = array[0]
    a = array[1]
    b = array[2]
    c = array[3]
    x = ["平时成绩", "实验成绩", "卷面成绩"]
    y = [a, b, c]
    plt.title(name)
    plt.bar(x, y)
    plt.show()
