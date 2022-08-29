print("你是谁？")
name = input()
print(name)
print("你是%s" % name)

name2 = input("你又是谁？")
print("你是" + name2)

# input输入的默认为字符串类型
# 输入内容判断类型
nwrs = input("请输入内容：")
print("你输入的内容类型是：", type(nwrs))

# 输入内容转换成数字类型
uuzi = input("请输入一个数字：")
print("你输入的数字类型是：", type(int(uuzi)))

# 练习
user_name = input("你是？")
user_type = input("你的等级是？")
print(f"你好：{user_name}，您是尊贵的：{user_type}用户，欢迎你的光临。")
