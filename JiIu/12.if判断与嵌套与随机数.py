age = 19
if age >= 18:
    print("成年了！")
else:
    print("未成年！")

print("hahaha")

# Python通过首行缩进(4个空格)来判断那个代码块属于哪个if

# 练习猜数字
"""
age = 19
if age == int(input("请输入第一次猜想的数字：")):
    print("猜对了")
elif age == int(input("不对，再猜一次：")):
    print("猜对了")
elif age == int(input("最后再猜一次：")):
    print("猜对了")
else:
    print(f"全错了，正确答案是：{age}")
"""

# if嵌套练习        嵌套的关键在于空格缩进，通过空格缩进，来决定语句之间的：层次关系
"""
user_name = input("请设置用户名：")
user_psd = input("请设置密码：")
print("现在进行登录")
if input("请输入用户名：") == user_name:
    print("用户名正确！")
    if input("请输入密码：") == user_psd:
        print("密码正确！")
    else:
        print("密码错误！")
else:
    print("用户名错误！")
"""

# 实战&随机数
# 需求：
# · 定义一个数字（1~10，随机产生），通过三次判断来猜出数字
# 要求：
# 1.数字随机产生，范围1-10
# 2.有3次机会猜测数字，通过3层嵌套判断实现
# 3.每次猜不中，会提示大了或小了
""" 随机数代码，num变量储存随机数字
import random
num = random.randint(1, 10)
"""

"""
import random

num = random.randint(1, 10)
# print(num)
num2 = int(input("第一次猜测："))
if num == num2:
    print("猜对了")
else:
    if num2 > num:
        print("大了")
    else:
        print("小了")
    num2 = int(input("第二次猜测："))
    if num == num2:
        print("猜对了")
    else:
        if num2 > num:
            print("大了")
        else:
            print("小了")
        num2 = int(input("第三次猜测："))
        if num == num2:
            print("猜对了")
        else:
            if num2 > num:
                print("大了")
            else:
                print("小了")
print(f"正确答案是：{num}")
"""
