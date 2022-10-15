while True:
    print("\n1.长方形 \n2.正方形 \n3.圆形 \n0.退出")
    xv = int(input("请输入你要计算的形状的编号："))
    andAll = 0
    if xv == 1:
        length = eval(input("请输入长方形的长："))
        width = eval(input("请输入长方形的宽："))
        andAll = length * width
        if andAll < 0:
            print("输入有误")
        else:
            print("面积为：", andAll)
    elif xv == 2:
        print()
    elif xv == 3:
        PI = 3.14

    elif xv == 0:
        break
    else:
        print("输入错误，请重输")
