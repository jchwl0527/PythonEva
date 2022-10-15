# 读取文件内容并输出

with open("3.txt", mode='r', encoding='utf-8') as f:
    area = 0
    while True:
        list01 = f.readline()  # 分割字符串
        while list01 != "":
            lis01 = list01.split()
            if lis01[0] == "正方形":
                area = eval(lis01[1]) ** 2
            print(list01[0], "面积为：", area)
            break
    while True:
        list02 = f.readline()  # 分割字符串
        while list02 != "":
            lis02 = list02.split()
            if lis02[0] == "长方形":
                area = eval(lis02[1]) ** 2
            print(list02[0], "面积为：", area)
            break
