"""
- 内容限定
- 大小写敏感(大小写可区分)
- 不可使用关键字
- 只允许出现：英文，中文(不推荐)，数字(不可在开头)，下划线(_)
"""

# 大小写敏感
Num = "大写"
num = "小写"
print(Num, num)

# 不可使用关键字
# class = 1     不可运行
# def = 2       不可运行
Class = 3  # 可运行
Def = 4  # 可运行
print(Class, Def)
