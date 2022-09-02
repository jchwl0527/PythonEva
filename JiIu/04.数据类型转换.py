# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(12.34)
print(type(float_str), float_str)
# 将字符串转换成数字
num = int(11)
print(type(num), num)

num2 = float("12.345")
print(type(num2), num2)
# 将字符串转换成数字，必须要求字符串内的内容都是数字

# 整数转换浮点数
float_num = float(12)
print(type(float_num), float_num)

# 浮点数转整数
int_num = int(12.345)
print(type(int_num), int_num)

# 非同类型未转换不能进行计算
"""
no1 = 1
no2 = "2"
print(no1 + no2)
"""
# 转换类型进行计算
no3 = 3
no4 = "4"
print(type(no3 + int(no4)), no3 + int(no4))
