# 数据容器
# 一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素
# 每一个元素，可以是任意类型的数据，如字符串、数字、布尔等。
# 数据容器根据特点的不同，如：
# 是否支持重复元素
# 是否可以修改
# 是否有序，等
# 分为5类，分别是：
# 列表（list）、元组（tuple）、字符串（str）、集合（set）、字典（dict）
# 注意：列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套
# """
# my_list = ['a5', 'b', 'c', True, 1, ['d', 'e', False, ['f', 4, True]], ['h', 3, False]]
# print(my_list)
# print(type(my_list))
# """

#  字面量
# [元素1, 元素2, 元素3, 元素4]

# 定义变量
# 变量名称 = [元素1, 元素2, 元素3, 元素4]

# 定义空变量
# 变量名称 = []
# 变量名称 = list()

# 列表的下标(索引)
# 元素有顺序，从左向右，第一个为 0 ，依次递增
# 元素有顺序，从右向左，第一个为 -1 ，依次递减
# 超出范围会报错
"""
my_list = ['a5', 'b', 'c', True, 1, ['d', 'e', False, ['f', 4, True]], ['h', 3, False]]
print(my_list[0])
print(my_list[3])
print(my_list[4])
print(my_list[5])
print(my_list[-1])
"""

# 去除嵌套列表中的元素
# """
# 1
# num = my_list[5]
# print(num[1])
# 2
# print(my_list[5][1])
# """

# 函数是一个封装的代码单元，可以提供特定功能。
# 在Python中，如果将函数定义为class（类）的成员，那么函数会称之为：方法
"""
# 函数
def add(x, y):
    return x + y


# 调用
print(add(1, 2))


# 方法
class Student:
    def add(self, x, y):
        return x + y


# 调用
student = Student()
# num = student.add(2, 3)
# print(num)
print(student.add(2, 3))
"""

# 列表的查询功能（方法）
# 查找指定元素在列表的下标，找不到会报错ValueError
# 语法：列表.index(元素)
# index就是列表对象（变量）内置的方法（函数）
"""
syr_list = ['a5', 'b', 'c', 'd', ]
index = syr_list.index('c')
print(index)
"""

# 列表的修改功能（方法）
# 修改
# 语法：列表[下标] = 值
"""
syr_list = ['a5', 'b', 'c', 'd', ]
print(syr_list)
syr_list[2] = 'cc'
print(syr_list)
"""

# 插入
# 语法：列表.insert(下标, 元素)，在指定的下标位置，插入指定的元素
"""
syr_list = ['a5', 'b', 'c', 'd', ]
print(syr_list)
syr_list.insert(3, 'ccc')
print(syr_list)
"""

# 追加1
# 语法：列表.append(元素)，将指定元素，追加到列表的尾部
"""
syr_list = ['a5', 'b', 'c', 'd', ]
print(syr_list)
syr_list.append('f', )
print(syr_list)
syr_list.append(['h', 'i'])
print(syr_list)
"""

# 追加2
# 语法：列表.extend(其它数据容器)，将其他数据容器的内容取出，依次追加到列表尾部
"""
syr_list = ['a5', 'b', 'c', 'd', ]
print(syr_list)
syr_list.extend(['f', 'h', 'i'])
print(syr_list)
"""

# 删除元素
# 语法1: del 列表[下标]
# 语法2: 列表.pop(下标)   同等与 取出
"""
syr_list = ['a5', 'b', 'c', 'd', ]
print(syr_list)
del syr_list[1]
print(syr_list)
num = syr_list.pop(1)
print(syr_list)
print(num)
"""

# 删除某元素在列表中的第一个匹配项
# 语法: 列表.remove(元素)
"""
syr_list = ['a5', 'b', 'c', 'd', 'b']
print(syr_list)
syr_list.remove('b')
print(syr_list)
"""

# 清空列表内容
# 语法: 列表.clear()
"""
syr_list = ['a5', 'b', 'c', 'd', 'b']
print(syr_list)
syr_list.clear()
print(syr_list)
"""

# 统计某元素在列表中的数量
# 语法: 列表.count(元素)
"""
syr_list = ['a5', 'b', 'c', 'd', 'b']
num = syr_list.count('b') 
print(num)
"""

# 统计列表中全部的元素数量
# 语法: len(列表)
"""
syr_list = ['a5', 'b', 'c', 'd', 'b']
print(len(syr_list))
"""

# 练习
# age = [21, 25, 21, 23, 22, 20]
# age.append(31)
# print(age)
# age.extend([29, 33, 30])
# print(age)
# print(age[0])
# print(age.pop(-1))
# print(age.index(31))
