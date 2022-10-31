# def 函数(参数...):
#     函数体
#     return 返回值    函数遇到return之后就结束了，不会执行后面的代码
# 变量 = 函数(参数)

# 有返回值调用正常返回值
def syr_add(a, b):
    result = a + b
    return result
    # return a5 + b


# i = syr_add(1, 2)
# print(i)
print(syr_add(1, 2))


# 无返回值调用返回字面量None
def syr_add(a, b):
    a + b


# i = syr_add(1, 3)
# print(i)
print(syr_add(1, 3))
print(type(syr_add(1, 3)))  # 返回结果为None，返回类型为NoneType，意为空的，无意义的。表示这个函数没有放回有意义的内容。


# 手动返回None与return返回的None一样

# 在if判断中，None等同于False假，一般用于在函数中主动返回None，配合if判断做相关处理
def syr_age(age):
    if age >= 18:
        return "SUCCESS"
    else:
        return None


result = syr_age(16)
if not result:  # 如果返回值是False，就执行下面的代码
    # 进入if表示result是None值，也就是False
    print("未成年不可入内")

# 用于声明无内容的变量上，定义变量，但暂时不需要变量有具体值，可以用None来代替
name = None
print(f"{name},{type(name)}")
