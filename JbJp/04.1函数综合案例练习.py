# 定义一个全局变量:money,用来记录银行卡余额（默认50000000）
# 定义一个全局变量：name,用来记录客户姓名（启动程序时输入）
# 定义如下的函数：
# 查询余额函数
# 存款函数
# 取款函数
# 主菜单函数
# 要求:
# 程序启动后要求输入客户姓名
# 查询余额、存款、取款后都会返回主菜单
# 存款、取款后，都应显示一下当前余额
# 客户选择退出或输入错误，程序会退出，否则一直运行

money = 50000000
name = None


# 主菜单函数
def main():
    print("-----------------主菜单-----------------")
    print(f"{name}，你好，欢迎来到卡塞尔学院附属银行，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入0]")
    syr_homes = int(input("请输入你的选择："))
    if syr_homes == 1:
        syr_yuer(True)
        main()
    elif syr_homes == 2:
        syr_cunkuan()
        main()
    elif syr_homes == 3:
        syr_qukuan()
        main()
    elif syr_homes == 0:
        print("正在退出")
        exit()
    else:
        print("输入错误，即将退出")
        exit()


# 查询余额函数
def syr_yuer(show_header):
    if show_header:
        print("--------------查询余额--------------")
    yuer = str(print(f"{name}，你好，当前余额为{money}元"))
    # return yuer


# 存款函数
def syr_cunkuan():
    global money
    print("----------存款----------")
    syr_cunkuans = int(input("请输入存款金额："))
    money = money + syr_cunkuans
    # money = data + money  弃用局部变量方案
    print(f"{name}，你好，你存款{syr_cunkuans}元成功！")
    # return syr_yuer(False)


# 取款函数
def syr_qukuan():
    global money
    print("----------取款----------")
    syr_qukuans = int(input("请输入取款金额："))
    if money > 0:
        money = money - syr_qukuans
        # money = money - data  弃用局部变量方案
        print(f"{name}，你好，你存款{syr_qukuans}元成功！")
    else:
        print(f"{name}，你好，你当前余额为{money}，没钱了还想取款，想着吧！")
    # return syr_yuer(False)


# if __name__ == '__main__':
while True:
    name = input("请输入你的姓名：")
    print(main())
