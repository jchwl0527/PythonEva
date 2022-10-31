# 导包
import os

import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取文件
nums = open("2.csv", mode='r', encoding='utf8', )
# 获取文件中所有行的列表
num = nums.readlines()
# 关闭文件
nums.close()
# 检测图片储存目录是否存在
os_path = './img2/'
if os.path.exists(os_path):
    print("存在")
else:
    print("不存在，正在创建")
    # 创建图片存放目录
    os.mkdir('./img2/')
# 循环读取数据进行处理
for line in num:
    nums = line.split(",")
    name = nums[0]
    a = int(nums[1])
    b = int(nums[2])
    c = int(nums[3])
    x = ["平时成绩", "实验成绩", "卷面成绩"]
    y = [a, b, c]
    # 生成并设置颜色为花色
    plt.bar(x, y)
    plt.title(name)
    # 保存数据输出图片
    plt.savefig('./img2/' + name + '.png')
    # 展示图片
    plt.show()
