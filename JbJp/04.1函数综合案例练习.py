# 定义一个全局变量:money,用来记录银行卡余额（默认50000000）
# 定义一个全局变量：name,用来记录客户姓名（启动程序时输入）
# 定义如下的函数：
# 查询余额函数
# 存款函数
# 取款函数
# 主菜单函数
# 要求:
# todo 程序启动后要求输入客户姓名
# 查询余额、存款、取款后都会返回主菜单
# 存款、取款后，都应显示一下当前余额
# 客户选择退出或输入错误，程序会退出，否则一直运行

money = 50000000
name = None


# 主菜单函数
def syr_home():
    syr_homes = int(input("查询余额请输入1\t存款请输入2\t取款请输入3\t退出请输入0\t"))
    if syr_homes == 1:
        syr_yuer()
        syr_home()
    elif syr_homes == 2:
        syr_cunkuan()
        syr_home()
    elif syr_homes == 3:
        syr_qukuan()
        syr_home()
    elif syr_homes == 0:
        print("正在退出")
        exit()
    else:
        print("输入错误，即将退出")
        exit()


# 查询余额函数
def syr_yuer():
    yuer = str(print(f"当前余额为{money}元"))
    return yuer


# 存款函数
def syr_cunkuan():
    global money
    money = money + int(input("请输入存款金额："))
    # money = data + money  弃用局部变量方案
    return syr_yuer()


# 取款函数
def syr_qukuan():
    global money
    money = money - int(input("请输入取款金额："))
    # money = money - data  弃用局部变量方案
    return syr_yuer()


if __name__ == '__main__':
    print(syr_home())
