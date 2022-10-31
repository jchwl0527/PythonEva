# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
# plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆
# label = ['第一', '第二', '第三']  # 定义饼图的标签，标签是列表
# explode = [0.01, 0.01, 0.01]  # 设定各项距离圆心n个半径
# # plt.pie(values[-1,3:6],explode=explode,labels=label,autopct='%1.1f%%')#绘制饼图
# values = [1, 2, 7]
# plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
# plt.title('2018年饼图')  # 绘制标题
# plt.savefig('./2018年饼图')  # 保存图片
# plt.show()


# import matplotlib.pyplot as plt
#
# # 这两行代码解决 plt 中文显示的问题
# from zoye.duqu import fileHandler
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# listOfLines = fileHandler.readlines()
# fileHandler.close()
#
# for line in listOfLines:
#     array = line.split(",")
#     name = array[0]
#     a = array[1]
#     b = array[2]
#     c = array[3]
#     x = ["平时成绩", "实验成绩", "卷面成绩"]
#     y = [a, b, c]
#     plt.title(name)
#     plt.bar(y, x)
#     plt.show()
