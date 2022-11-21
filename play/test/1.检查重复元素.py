# 下面的方法可以检查给定列表中是否有重复的元素。它使用了set()属性，该属性将会从列表中删除重复的元素。

def all_unique(lst):
    # return len(lst) == len(set(lst))
    print(len(lst) == len(set(lst)))
    print(set(lst))  # 输出不重复的元素


x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]
all_unique(x)  # False
all_unique(y)  # True
