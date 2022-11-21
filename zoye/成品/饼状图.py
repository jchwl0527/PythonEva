# 导包
import os

import matplotlib.pyplot as plt
import pandas as pd

# 替换考勤表数据内容
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
# 计算考勤表分数
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

# 读取成绩表源文件
df2 = pd.read_excel('成绩表.xlsx', header=None)
# 清洗数据
df2 = df2.drop([0])
# 输出CSV文件
df2.to_csv('成绩表.csv', header=None, index=False)
# 读取
results = open("成绩表.csv", mode='r', encoding='utf8')
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
# 设置成绩等级
excellent = 0
good = 0
secondary = 0
garbage = 0

for lens in n:
    if 100 > int(lens) >= 90:
        excellent = excellent + 1
    elif 90 > int(lens) >= 75:
        good = good + 1
    elif 75 > int(lens) >= 60:
        secondary = secondary + 1
    else:
        garbage = garbage + 1

t = excellent + good + secondary + garbage
comprehensive = [excellent / t, good / t, secondary / t, garbage / t]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

labels = ['优', '良', '中', '差']

# 检测图片储存目录是否存在
os_path = './饼状图/'
if os.path.exists(os_path):
    print("存在")
else:
    print("不存在，正在创建")
    # 创建图片存放目录
    os.mkdir('./饼状图/')

plt.pie(comprehensive, labels=labels, autopct='%0.2f%%', colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"])
plt.title("学生成绩比例")
plt.savefig('./饼状图/学生成绩比例.png')
plt.show()
