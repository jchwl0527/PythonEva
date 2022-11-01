# 因为不确定有几个成绩表文件，所以写了两个文件的读取，并注释了一个

# 导包
import os

import matplotlib.pyplot as plt
import pandas as pd

# 读取源文件
df = pd.read_excel('成绩表.xlsx')
# df2 = pd.read_excel('成绩单2.xlsx')
# 删除不需要的内容
# df2 = df2.drop([0, 1])
# 输出无索引行的CSV文件
df.to_csv('成绩表.csv', header=False, index=False)
# df2.to_csv('csv2.csv', header=False, index=False)

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取文件
num1 = open("成绩表.csv", mode='r', encoding='utf8', )
# num2 = open("csv2.csv", mode='r', encoding='utf8', )
# 获取文件中所有行的列表
numa = num1.readlines()
# numb = num2.readlines()
# 多个文件内容相加 / 多余
numc = numa  # + numb
# 关闭文件
num1.close()
# num2.close()
# 检测图表输出目录是否存在
os_path = './柱状图/'
if os.path.exists(os_path):
    print("存在")
else:
    print("不存在，正在创建")
    # 创建图片存放目录
    os.mkdir('./柱状图/')
# 循环读取数据进行处理
for line in numc:
    nums = line.split(",")
    name = nums[0]
    a = int(nums[1])
    b = int(nums[2])
    c = int(nums[3])
    x = ["平时成绩", "实验成绩", "卷面成绩"]
    y = [a, b, c]
    # 生成图表
    plt.bar(x, y)
    # 设置标题
    plt.title(name)
    # 输出图表
    plt.savefig('./柱状图/' + name + '.png')
    # 展示图片，如不展示将出现莫名颜色错误
    plt.show()
