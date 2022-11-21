import os

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('成绩表.xlsx')
df.to_csv('chengjibiao.csv', header=False, index=False)

df = pd.read_excel('成绩表.xlsx')
df.to_csv('成绩表.csv', index=False)
df1 = pd.concat([df.姓名] + [df.平时], axis=1)
df1.to_csv('pingshi.csv', index=False)
df1 = pd.concat([df.姓名] + [df.实验], axis=1)
df1.to_csv('shiyan.csv', index=False)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

num1 = open("chengjibiao.csv", mode='r', encoding='UTF8', )
numa = num1.readlines()
num1.close()
for line in numa:
    nums = line.split(",")
    name = nums[0]
    a = int(nums[1])
    b = int(nums[2])
    c = int(nums[3])
    x = ["平时成绩", "实验成绩", "卷面成绩"]
    y = [a, b, c]
    plt.bar(x, y)
    plt.title(name)
    plt.savefig('./img/' + name + '.png')

with open("pingshi.csv", mode='r', encoding='UTF8') as fin1:
    with open("shiyan.csv", mode='r', encoding='UTF8') as fin2:
        with open("scoreresult.csv", mode='w', encoding='UTF8') as fout:
            mydata1 = fin1.readline()
            mydata1 = fin1.readline()
            mydata2 = fin2.readline()
            mydata2 = fin2.readline()
            totalscore = 0
            list01 = []
            list02 = []
            while mydata1 != "":
                str01 = mydata1.split(',')
                str02 = mydata2.split(',')
                totalscore = eval(str01[1]) * 0.1 + eval(str02[1]) * 0.2
                list01.append(str01[0])
                list02.append(totalscore)
                fout.write(str01[0] + " " + str(totalscore) + "\n")
                mydata1 = fin1.readline()
                mydata2 = fin2.readline()
plt.bar(list01, list02)
plt.savefig('./123.png')
fout.close()
fin1.close()
fin2.close()

df = pd.read_excel('考勤表.xlsx', header=None)
df.to_csv('考勤表.csv', header=None, index=False)
with open("考勤表.csv", "rt", encoding='UTF8') as file:
    x = file.read()
    with open("考勤表.csv", "wt", encoding='UTF8') as file:
        x = x.replace("V", "10")
        file.write(x)
        with open("考勤表.csv", "wt", encoding='UTF8') as file:
            x = x.replace("X", "-10")
            file.write(x)
            with open("考勤表.csv", "wt", encoding='UTF8') as file:
                x = x.replace("O", "-5")
                file.write(x)

file.close()
with open('考勤表.csv', 'rt', encoding='UTF8') as file:
    for line in file:
        nums = line.split(",")
        name = nums[0]
        s = nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7] + nums[8] + nums[9] + nums[10]

df2 = pd.read_excel('成绩表.xlsx', header=None)
df2 = df2.drop([0])
df2.to_csv('成绩表.csv', header=None, index=False)
results = open("成绩表.csv", mode='r', encoding='UTF8')
result = results.readlines()
results.close()
n = []
for line in result:
    nums = line.split(',')
    name = nums[0]
    a = int(nums[1]) * 0.1
    b = int(nums[2]) * 0.1
    c = int(nums[3]) * 0.7
    d = a + b + c + s * 0.1
    n.append(d)
a = 0
b = 0
c = 0
d = 0
for lens in n:
    if 100 > int(lens) >= 90:
        a = a + 1
    elif 90 > int(lens) >= 75:
        b = b + 1
    elif 75 > int(lens) >= 60:
        c = c + 1
    else:
        d = d + 1

t = a + b + c + d
comprehensive = [a, b, c, d]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
a1a = ['优', '良', '中', '差']
plt.pie(comprehensive, labels=a1a)
plt.savefig('./学生成绩比例.png')
