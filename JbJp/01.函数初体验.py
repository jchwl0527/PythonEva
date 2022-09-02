# # 统计字符串的长度，不适用内置函数len()
#
# str1 = "zxcvbnm"
# str2 = "zxcvbnmlp"
# str3 = "wubba lubba dab dab"
#
# # 定义一个计数的变量
# """
# count = 0
# for i in str1:
#     count += 1
# print(f"字符串{str1}的长度是{count}")
#
# count = 0
# for i in str2:
#     count += 1
# print(f"字符串{str2}的长度是{count}")
#
# count = 0
# for i in str3:
#     count += 1
# print(f"字符串{str3}的长度是{count}")
# """
#
#
# def syr_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度是{count}")
#
#
#
# syr_len(str1)
# syr_len(str2)
# syr_len(str3)
# 函数的定义
"""
def 函数名(传入参数):
    函数体
    return 返回值 (可省略)
"""


# 先定义后调用

def syr_hi():  # 没有传入参数也要写():
    print("人生苦短，我用Python")
    print("人生苦短\n我用Py")


# 调用函数  函数名(参数)     没有参数可以不写
syr_hi()


def syr_j(a, b):  # 函数可以使用任意n个参数
    c = a + b
    print(f"{a} + {b} = {c}")


syr_j(2, 1)


# 练习    体温判断

def syr_tiwf(tiwf):
    bnvy = 37.5
    if tiwf > bnvy:
        print(f"欢迎来到卡塞尔学院，你的体温是{tiwf}度，需要隔离！")
    else:
        print(f"欢迎来到卡塞尔学院，你的体温是{tiwf}，请进")


syr_tiwf(37.5)
