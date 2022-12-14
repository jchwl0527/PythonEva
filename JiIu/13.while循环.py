# while层次关系同样用空格缩进来处理
i = 0
while i < 100:
    print(i)
    i += 1

# 练习
"""
sum = 0
i = 1

while i <= 100:
    sum += i
    i += 1
print(sum)
"""

# 无限猜数字

"""
num = random.randint(1, 100)
i = 0
flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字："))
    i += 1
    if guess_num == num:
        print("猜中了")
        flag = False  # 终止循环
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")
print(f"你总共猜测了{i}次")
"""

# while的自我嵌套

"""
i = 1
while i <= 100:
    print(f"今天是第{i}天")

    i = 1
    while i <= 10:
        print(f"今天有{i}个")
        i += 1

    print("可以")
    i += 1
print(f"完事，共{i - 1}天")
"""

# 练习 九九乘法表
"""
i = 1
while i <= 9:

    i = 1
    while i <= i:
        print(f"{i} * {i} = {i * i}\t", end='')
        i += 1
    i += 1
    print()  # print空内容等于输出一个换行
"""
