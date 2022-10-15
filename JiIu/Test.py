"""
# # print输出不换行

print("Hello")  # 输出换行
print("World")

print("Hello", end='')  # 输出不换行
print("World")

# 制表符
# \t == Tab
print("Hello\tworld")
print("Hi\t\tworld")

a = 24
print(bin(a))   # 将整数x转换为二进制字符串﹐例如bin(24)结果是'0b11000'
print(oct(a))   # 将整数x转化为八进制字符串﹐例如oct(24)结果是'0o30
print(hex(a))   # 将整数x转换为十六进制字符串,例如hex(24)结果是'0x18'

i = complex(3, 5)   # 创建一个复数
print(i)
print(type(i))

print(int(2.2))
print(float(2))
print(str(4) + str(5))
print(eval("3 + 3 + 2"))    # 用来计算在字符串中的有效Python表达式并返回一个对象
"""
"""
i = 10
print(id(i))  # id 在创建时已分配给对象。id 是对象的内存地址，并且在每次运行程序时都不同。（除了某些具有恒定唯一 id 的对象，比如 -5 到 256 之间的整数）
print(ord("A"))  # 将一个字符转换为它的ASCII整数值(汉字为Unicode编码）
print(chr(65))  # 返回整数对应的ASCII字符
i = int(65)
print(chr(i))  # 返回整数对应的ASCII字符

a = 123
del a  # 删除变量
print(a)
"""

# 计算字符长度
name = "zxcvbnmlp"
print(len(name))
print(len("zxcvbnmlp"))

# 获取当前日期时间
from datetime import datetime

now = datetime.now()
print(str(now))

print(repr(now))
