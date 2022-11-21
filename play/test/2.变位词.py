# 检测两个字符串是否互为变位词（即互相颠倒字符顺序）
from collections import Counter


def anagram(first, second):
    # return Counter(first) == Counter(second)
    x = Counter(first) == Counter(second)

    print(x)


anagram("abcd3", "3acdb")  # True
