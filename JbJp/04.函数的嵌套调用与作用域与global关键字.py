# 嵌套调用
"""
def syr_b():
    print("2")


def syr_a():
    print("1")

    syr_b()

    print("3")


syr_a()
"""

# 作用域1，局部变量
# 所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效
"""
def syr_test1():
    num = 100
    print(num)


syr_test1()  # 100
print(num)  # 报错
"""
# 作用域2，全局变量
# 所谓全局变量，指的是在函数体内、外都能生效的变量
# 定义全局变量a
"""
num = 100


def syr_test2():
    print(num)


def syr_test3():
    print(num)


syr_test2()
syr_test3()
print(num)
"""

# 在函数内部修改全局变量
""" 直接改就是这样
num = 200


def syr_test4():
    print(f"syr_test4: {num}")


def syr_test5():
    num = 500  # 局部变量
    print(f"syr_test5: {num}")


syr_test4()
syr_test5()
print(num)
"""
# global关键词

num = 200


def syr_test4():
    print(f"syr_test4: {num}")


def syr_test5():
    # global关键字生命num是全局变量
    global num
    num = 500
    print(f"syr_test5: {num}")


syr_test4()
syr_test5()
print(num)
