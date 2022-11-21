# 以下代码段可用来检查对象的内存使用情况。
import sys

variable = 30
print(sys.getsizeof(variable))  # 24
