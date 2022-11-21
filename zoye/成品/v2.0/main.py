# 导包
import os
import matplotlib.pyplot as plt
import pandas as pd

# 设置plt中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 目录检测模块
# 检测图片输出目录是否存在，如不存在就创建
def osmkdir(path):
    if os.path.exists(path):
        print("---  文件夹被创建过了！  ---")
        print('正在保存图表，请稍后')
    else:
        os.mkdir(path)
        print("---  创建文件夹成功  ---")
        print('正在保存图表，请稍后')


# 考勤查询模块
def kqcl():
    df = pd.read_excel('考勤表.xlsx', header=None)
    df.to_csv('kaoqin.csv', header=None, index=False)
    with open("kaoqin.csv", "rt", encoding='utf-8') as file:
        x = file.read()
    with open("kaoqin.csv", "wt", encoding='utf-8') as file:
        x = x.replace("V", "10")
        file.write(x)
    with open("kaoqin.csv", "wt", encoding='utf-8') as file:
        x = x.replace("X", "-10")
        file.write(x)
    with open("kaoqin.csv", "wt", encoding='utf-8') as file:
        x = x.replace("O", "-5")
        file.write(x)
    file.close()


# 柱状图生成模块
def zhu():
    df = pd.read_excel('成绩表.xlsx')
    df.to_csv('成绩表.csv', index=False)
    # 分离数据
    df1 = pd.concat([df.姓名] + [df.平时], axis=1)
    df1.to_csv('pingshi.csv', index=False)
    df1 = pd.concat([df.姓名] + [df.实验], axis=1)
    df1.to_csv('shiyan.csv', index=False)
    df1 = pd.concat([df.姓名] + [df.期末], axis=1)
    df1.to_csv('qimo.csv', index=False)

    # 处理数据
    with open("pingshi.csv", mode='r', encoding='UTF8') as fin1:
        with open("shiyan.csv", mode='r', encoding='UTF8') as fin2:
            with open("qimo.csv", mode='r', encoding='UTF8') as fin3:
                with open("zongfen.csv", mode='w', encoding='UTF8') as fout1:
                    with open("pingjun.csv", mode='w', encoding='UTF8') as fout2:
                        mydata1 = fin1.readline()
                        mydata1 = fin1.readline()
                        mydata2 = fin2.readline()
                        mydata2 = fin2.readline()
                        mydata3 = fin3.readline()
                        mydata3 = fin3.readline()
                        list01 = []
                        list02 = []
                        list03 = []
                        # 调用osmkdir()模块进行判断目录并创建
                        paths = str(input("请输入柱状图要保存的位置："))
                        osmkdir(paths)
                        # 求总分和平均分
                        while mydata1 != "":
                            str01 = mydata1.split(',')
                            str02 = mydata2.split(',')
                            str03 = mydata3.split(',')
                            zongFen = eval(str01[1]) + eval(str02[1]) + eval(str03[1])
                            pingJun = zongFen / 3
                            print(str01[0] + "的总成绩为：" + str(zongFen))
                            print(str01[0] + "的平均成绩为：" + "%.2f" % pingJun)
                            list01.append(str01[0])
                            list02.append(zongFen)
                            fout1.write(str01[0] + "," + str(zongFen) + "\n")
                            fout2.write(str01[0] + "," + str("%.2f" % pingJun) + "\n")
                            mydata1 = fin1.readline()
                            mydata2 = fin2.readline()
                            mydata3 = fin3.readline()
                            # 个人成绩柱状图生成部分
                            x = ["平时成绩", "实验成绩", "卷面成绩"]
                            y = [int(str01[1]), int(str02[1]), int(str03[1])]
                            plt.title(str01[0])
                            plt.bar(x, y, color=["#4CAF50", "hotpink", "#556B2F"])
                            # 保存图表
                            plt.savefig(paths + '/' + str01[0] + '.png')
                            # 展示图表
                            plt.show()


# 饼状图生成模块
def bing(TF):
    kqcl()
    # 计算考勤表分数
    with open('kaoqin.csv', 'rt', encoding='utf-8') as file:
        for line in file:
            num = line.split(",")
            name = num[0]
            num[1] = int(num[1])
            num[2] = int(num[2])
            num[3] = int(num[3])
            num[4] = int(num[4])
            num[5] = int(num[5])
            num[6] = int(num[6])
            num[7] = int(num[7])
            num[8] = int(num[8])
            num[9] = int(num[9])
            num[10] = int(num[10])
            s = num[1] + num[2] + num[3] + num[4] + num[5] + num[6] + num[7] + num[8] + num[9] + num[10]
    df2 = pd.read_csv('成绩表.csv', header=None)
    df2 = df2.drop([0])
    df2.to_csv('成绩表.csv', header=None, index=False)
    results = open('成绩表.csv', mode='r', encoding='utf8')
    result = results.readlines()
    results.close()

    bili1 = int(input("请输入平时成绩的占比：")) / 10
    bili2 = int(input("请输入实验成绩的占比：")) / 10
    bili3 = int(input("请输入期末成绩的占比：")) / 10
    n = []
    excellent = 0
    good = 0
    secondary = 0
    garbage = 0
    for line in result:
        nums = line.split(',')
        name = nums[0]
        a1 = int(nums[1]) * bili1
        a2 = int(nums[2]) * bili2
        a3 = int(nums[3]) * bili3
        d = a1 + a2 + a3 + s * 0.1
        n.append(d)
    for lens in n:
        if 100 > int(lens) >= 90:
            excellent = excellent + 1
        elif 90 > int(lens) >= 75:
            good = good + 1
        elif 75 > int(lens) >= 60:
            secondary = secondary + 1
        else:
            garbage = garbage + 1

    if TF == 'T':
        t = excellent + good + secondary + garbage
        comprehensive = [excellent / t, good / t, secondary / t, garbage / t]
        labels = ['优', '良', '中', '差']
        # 调用osmkdir()模块进行判断目录并创建
        paths = str(input("请输入饼状图要保存的位置："))
        osmkdir(paths)
        plt.pie(comprehensive, labels=labels, autopct='%0.2f%%', colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"])
        plt.title("学生成绩比例")
        # 保存图表
        plt.savefig(paths + '/学生成绩比例.png')
        # 展示图表
        plt.show()
    elif TF == 'F':
        print("优秀人数：", excellent)
        print("不及格人数：", garbage)


# 散点图生成模块
def san():
    # 调用osmkdir()模块进行判断目录并创建
    paths = str(input("请输入散点图要保存的位置："))
    osmkdir(paths)
    df = pd.read_excel('成绩表.xlsx')
    df.to_csv('成绩表.csv', index=False)
    df = pd.read_csv('成绩表.csv', encoding='UTF8')
    df = df.fillna(method='backfill')
    y = df['平时'] * 0.1 + df['实验'] * 0.1 + df['期末'] * 0.7
    plt.title('学生成绩散点图')
    plt.scatter(df.姓名, y)
    # 保存图表
    plt.savefig(paths + '/学生成绩散点图.png')
    # 展示图表
    plt.show()


# main()中输入错误报错模块
def print_error():
    print("你的输入有误，请重新输入")


# main函数
def main():
    print('1.生成柱状图')
    print('2.生成饼状图')
    print('3.生成散点图')
    print('4.优良查询')
    print('0.退出')
    syr = int(input("请输入您的选项："))
    # 判断输入内容
    if syr == 1:
        zhu()
        main()
    elif syr == 2:
        bing('T')
        main()
    elif syr == 3:
        san()
        main()
    elif syr == 4:
        bing('F')
        main()
    elif syr == 0:
        exit()
    else:
        print_error()
        main()


main()
