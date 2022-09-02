buer = 10 == 5
print(f"10 > 5的结果是：{buer},类型是：{type(buer)}")

zifu = "a" == "b"
print(f"a == b , {zifu} , 类型是{type(zifu)}")

"""
==  判断内容是否相等，满足为True，不满足为False，如a=3,b=3,则(a=b)为True
!=  判断内容是否不相等，满足为True，不满足为False，如a=1,b=3,则(a!=b)为True
>   判断运算符左侧内容是否大于右侧,满足为True,不满足为False，如a=7,b=3,则(a>b)为True
<   判断运算符左侧内容是否小于右侧，满足为True，不满足为False，如a=3,b=7,则(a<b)为True
>=  判断运算符左侧内容是否大于等于右侧，满足为True，不满足为False，如a=3,b=3,则(a>=b)为True
<=  判断运算符左侧内容是否小于等于右侧，满足为True，不满足为False，如a=3,b=3,则(a<=b)为True
"""
# 首字母大写
bool_1 = True
bool_2 = False
print(f"bool_1变量是{bool_1}，类型是{type(bool_1)}，bool_2变量是{bool_2}，类型是{type(bool_2)}")

bool_3 = 1 == 1
print(f"这样写也行{bool_3 == bool_1}")
