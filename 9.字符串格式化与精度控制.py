# 字符串格式化
"""
%s  将内容转换成字符串，放入占位位置
%d  将内容转换成整数，放入占位位置
%f  将内容转换成浮点型，放入占位位置
"""

name = "Syr"
num = "我是 %s" % name  # %表示占位符，s表示将变量变成字符串放入占位的地方
print(num)

num1 = "你好"
num2 = "Syr"
num3 = 19
num4 = "%s，我是%s，我今年%s岁了！" % (num1, num2, num3)  # 多个变量要用括号括起来，并按照占位的顺序填入
print(num4)

# 字符串格式化 - 数字精度控制
"""
使用辅助符号"m.n"来控制数据的宽度和精度
m，控制宽度，要求是数字（很少使用），设置的宽度小于数字本身，不生效
.n，控制小数点精度，要求是数字，会进行小数四舍五入
实例：
%5d：表示将整数的宽度控制在5位，如数字11，被设置为5d,就会变成：[空格][空格][空格]11，用三个空格补足
宽度。
%5.2f：表示将宽度控制为5，将小数点精度设置为2
小数点和小数部分也算入宽度计算。如，对11.345设置了%7.2f后，结果是：[空格][空格]11.35。2个空格补足宽
度，小数部分限制2位精度后，四舍五入为.35
%.2f：表示不限制宽度，只设置小数点精度为2，如11.345设置%.2f后，结果是11.35
"""

a1 = 12.34567
a2 = ".%4d" % a1
a3 = "%4.3f" % a1
a4 = "%.2f" % a1
print(a2)
print(a3)
print(a4)

# 字符串格式化 - 快速写法(不限数据类型，不做精度控制)

# 语法：f"内容{变量}"


name1 = "Syr"
age2 = 19.5
abc = "hello"
print(f"我是{name},我的年龄是{age2},{abc},world!")

# 字符串格式化 - 表达式的格式化
print("2 * 2 = %d" % (2 + 2))
print(f"1 + 2 = {1 + 2}")
print("字符串在Python中的类型是：%s" % type("字符串"))

# 字符串格式化练习题

name = "XlouS"  # 公司名
stock_price = 19.99  # 当前股价
stock_code = 62612  # 股票代码
stock_price_daily_growth_factor = 1.2  # 股票每日增长系数，浮点数类型
growth_days = 7  # 增长天数
stock_prices = stock_price * stock_price_daily_growth_factor ** growth_days

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, stock_prices))
