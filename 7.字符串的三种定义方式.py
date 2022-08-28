"""
1.单引号定义法：name = '你好'
2.双引号定义法：name = "你好"
3.三引号定义法：name = " " "你好" " " （无引号间空格）

三引号定义法，和多行注释的写法一样，同样支持换行操作。
使用变量接收它，它就是字符串
不使用变量接收它，就可以作为多行注释使用。
"""
# 单
name = '你好'
print(type(name))
# 双
name = "你好"
print(type(name))
# 三
name = """你好"""
print(type(name))
