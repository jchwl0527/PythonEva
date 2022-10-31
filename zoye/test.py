import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

plt.bar(x, y)
plt.show()
# 查询
# import pandas as pd
#
# df = pd.read_csv('44.csv')
#
# print(df.to_string())


# 转储
# import pandas as pd
#
# 三个字段 name, site, age
# nme = ["Google", "Runoob", "Taobao", "Wiki"]
# st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
# ag = [90, 40, 80, 98]
#
# 字典
# dict = {'name': nme, 'site': st, 'age': ag}
#
# df = pd.DataFrame(dict)
#
# 保存 dataframe
# df.to_csv('site.csv')

# 查询开头部分行
# import pandas as pd
#
# df = pd.read_csv('44.csv')
#
# print(df.head(10))


# 查询结尾部分行
# import pandas as pd
#
# df = pd.read_csv('44.csv')
#
# print(df.tail(10))
