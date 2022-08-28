# type()输出结果可用print()打印出来
print("1")
print(type("你好"))
print(type(123))
print(type(2e3))  # 2e3 = 2000.0  2e-3 = 0.002

# type()输出的结果可用变量储存
print("2")
string_type = type("str")
int_type = type(123)
float_type = type(2e3)

print(string_type)
print(int_type)
print(float_type)

# type() 可以查看变量中存储的数据类型
print("3")
name = "你好"
name_type = type(name)
print(name_type)