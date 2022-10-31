import os

import matplotlib.pyplot as plt
import pandas as pd

# 考勤表
df = pd.read_excel('考勤表.xlsx', header=None)
df.to_csv('考勤表.csv', header=None, index=False)

with open("考勤表.csv", "rt", encoding='utf-8') as file:
    x = file.read()

with open("考勤表.csv", "wt", encoding='utf-8') as file:
    x = x.replace("V", "10")
    file.write(x)
with open("考勤表.csv", "wt", encoding='utf-8') as file:
    x = x.replace("X", "-10")
    file.write(x)
with open("考勤表.csv", "wt", encoding='utf-8') as file:
    x = x.replace("O", "-5")
    file.write(x)
file.close()
m = []
with open('考勤表.csv', 'rt', encoding='utf-8') as file:
    for line in file:
        nums = line.split(",")
        name = nums[0]
        nums[1] = int(nums[1])
        nums[2] = int(nums[2])
        nums[3] = int(nums[3])
        nums[4] = int(nums[4])
        nums[5] = int(nums[5])
        nums[6] = int(nums[6])
        nums[7] = int(nums[7])
        nums[8] = int(nums[8])
        nums[9] = int(nums[9])
        nums[10] = int(nums[10])
        s = nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7] + nums[8] + nums[9] + nums[10]

# 成绩表
df2 = pd.read_excel('成绩表.xlsx', header=None)
df2.to_csv('成绩表.csv', header=None, index=False)

results = open("成绩表.csv", mode='r', encoding='utf8', )
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

you = 0
liang = 0
zhong = 0
cha = 0

for len in n:
    if 100 > int(len) >= 90:
        you = you + 1
    elif 90 > int(len) >= 75:
        liang = liang + 1
    elif 75 > int(len) >= 60:
        zhong = zhong + 1
    else:
        cha = cha + 1

t = you + liang + zhong + cha
zong = [you / t, liang / t, zhong / t, cha / t]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

labels = ['优', '良', '中', '差']

# 检测图片储存目录是否存在
os_path = './bing2/'
if os.path.exists(os_path):
    print("存在")
else:
    print("不存在，正在创建")
    # 创建图片存放目录
    os.mkdir('./bing2/')

plt.pie(zong, labels=labels, shadow=True)
plt.savefig('./bing2/1.png')
