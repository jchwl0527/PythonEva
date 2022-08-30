# 遍历字符串
"""
name = "zxcvbnmlp"
for x in name:
    # 将name的内容，挨个取出赋予x临时变量进行处理
    print(x)
"""

# 练习    查找字符串中共有几个a
"""
name = "Wubba lubba dab dab!"
i = 0
for x in name:
    if x == "a":
        i += 1
    print(x, end='')
print(f"中共有{i}个字母a")
"""

# range获得一个简单的数字序列
# range 语法1
"""
num = 5
num1 = range(num)  # 获取从0开始，到num结束的数字序列，不包含num本身
print(num1)
for num2 in num1:
    print(num2)
print()
"""

# range 语法2
"""
num = 2
num1 = 8
num2 = range(num, num1)  # 获得一个从num开始，到num1结束的数字序列，不包含num1本身
print(num2)
for num3 in num2:
    print(num3)
print()
"""

# range 语法3
"""
num = 1
num1 = 9
step = 2  # 数字之间的步长，以step为准，step默认为1
num2 = range(num, num1, step)
print(num2)
for num3 in num2:
    print(num3)
"""

# 练习    有几个偶数
"""
num = 100
num1 = range(1, num)
i = 0
for num2 in num1:
    num2 = num2 % 2
    if num2 == 0:
        i += 1

print(f"1到{num}(不包含{num})范围内，有{i}个偶数。")
"""

# for   嵌套循环
"""
num2 = 0  # 规范代码
num1 = range(1, 11)
for num2 in num1:
    print(f"第{num2}天")
    for num2 in num1:
        print(f"第{num2}朵")
    print("送花结束")
print(f"第{num2}天，功德圆满")
"""

# 另一种
"""
num1 = 0  # 规范代码
num = range(1, 101)
Hua = range(1, 11)
for num1 in num:
    print(f"第{num1}天")
    for Hua1 in Hua:
        print(f"第{Hua1}朵")
print(f"第{num1}天，功德圆满")
"""
