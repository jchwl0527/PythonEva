# str(x)和repr(x)有何区别？

# print(str('123'))
# print(repr('123'))

# j = 30 - 3 ** 2 + 8 // 3 ** 2 * 10
# print(j)
#
# j = 3 * 4 ** 2 / 8 % 5
# print(j)


# import math
#
# print(math.ceil(10.2))
#
# from math import floor
#
# print(floor(10.5))

# import random
#
# i = random.random(10, 20)
# print(i)

# import time
#
# num = time.time()
# print(num)

# while True:
#
#     x = eval(input("请输入一个整数: "))
#     if x % 2 == 0:
#         print("偶数")
#         print("正常")
#     elif x < 0:
#         print("负奇数")
#         print("负数!")
#     else:
#         print("正奇数")
#         print("正数!")

# suma = 0
# i = 1
# while i <= 100:
#     suma += i
#     print(suma, i)
#     i += 1

for i in range(1, 11, 3):
    print(i)
