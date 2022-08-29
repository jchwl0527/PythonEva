age = 19
if age >= 18:
    print("成年了！")
else:
    print("未成年！")

print("hahaha")

# Python通过首行缩进(4个空格)来判断那个代码块属于哪个if

# 练习猜数字
# age = 19
# if age == int(input("请输入第一次猜想的数字：")):
#     print("猜对了")
# elif age == int(input("不对，再猜一次：")):
#     print("猜对了")
# elif age == int(input("最后再猜一次：")):
#     print("猜对了")
# else:
#     print(f"全错了，正确答案是：{age}")


# if嵌套练习        嵌套的关键在于空格缩进，通过空格缩进，来决定语句之间的：层次关系
# user_name = input("请设置用户名：")
# user_psd = input("请设置密码：")
# print("现在进行登录")
# if input("请输入用户名：") == user_name:
#     print("用户名正确！")
#     if input("请输入密码：") == user_psd:
#         print("密码正确！")
#     else:
#         print("密码错误！")
# else:
#     print("用户名错误！")
