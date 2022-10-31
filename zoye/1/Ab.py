# import time

import pandas as pd

# 用于记录程序运行时间
# start = time.time()

df = pd.read_excel('考勤表.xlsx', header=None)
df.to_csv('考勤表.csv', header=None, index=False)
num = pd.read_csv(open('考勤表.csv', mode="r", encoding="utf-8"))

with open("考勤表.csv", "rt", encoding='utf-8') as file:
    x = file.read()

with open("考勤表.csv", "wt", encoding='utf-8') as file:
    x = x.replace("V", "10")
    file.write(x)
with open("考勤表.csv", "wt", encoding='utf-8') as file:
    x = x.replace("X", "-10")
    file.write(x)
with open("考勤表.csv", "wt", encoding='utf-8') as file:
    x = x.replace("O", "-5")
    file.write(x)
file.close()

with open('考勤表.csv', 'rt', encoding='utf-8') as file:
    # num1 = file.read()
    for line in file:
        nums = line.split(",")
        name = nums[0]
        nums[1] = int(nums[1])
        nums[2] = int(nums[2])
        nums[3] = int(nums[3])
        nums[4] = int(nums[4])
        nums[5] = int(nums[5])
        nums[6] = int(nums[6])
        nums[7] = int(nums[7])
        nums[8] = int(nums[8])
        nums[9] = int(nums[9])
        nums[10] = int(nums[10])
        s = nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7] + nums[8] + nums[9] + nums[10]
        print(s)

# end = time.time()
# print(end - start)  # 查看程序运行时间
