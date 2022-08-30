# continue关键字用于：中断本次循环，直接进入下一次循环
# break关键字用于：直接结束循环
# continue，break    可以用于：for循环和while循环，效果一致
# continue，break    嵌套只能作用于本循环，不可对父循环生效

"""
for i in range(0, 10):
    print(i)
    continue
    print(i + 1)
"""
"""
for i in range(0, 10):
    print(i)
    break
    print(i + 1)
"""
"""
for i in range(0, 10):
    print(i)
    for j in range(1, 11):
        print(j)
        break
        print(j + 1)
    print(i + 1)
"""

# 练习
"""
money = 10000
# user_id = range(1, 21)
for num in range(1, 21):  # 控制行数
    import random

    user_jixn = random.randint(1, 11)
    if money > 0:
        if user_jixn < 5:  # 控制每行输出
            print(f"员工{num}，绩效分{user_jixn}，低于5，不发工资，下一位。")
        else:
            money -= 1000
            print(f"向员工{num}发放工资1000 账户余额还剩余{money}元")
    else:
        break
print("公司没钱了！")
"""

# 另一版本
"""
money = 10000
for i in range(1, 21):
    import random

    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}绩效分{score}，不满足，滚吧，下一个")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}，满足条件发工资1000元，公司余额：{money}")
    else:
        print(f"公司余额就剩{money}了")
        break        
"""
