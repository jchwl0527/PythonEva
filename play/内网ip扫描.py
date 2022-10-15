""" 扫描并保存
import win32api
import win32con


def msgbox(msg, title='提醒'):
    win32api.MessageBox(0, msg, title, win32con.MB_OK)


def local_ip_mac():  # 本机IP和MAC
    output = os.popen('ipconfig /all')
    for i in output:
        if '物理地址.' in i:
            mac = i.split(':')[1].strip()
        if 'IPV4' in i.upper() and '(' in i:
            ip = i.split(':')[1].split('(')[0].strip()
    if ip and mac:
        return [ip, mac]


def lan_ip_mac():  # 局域网IP和MAC
    ls = []
    output = os.popen('arp -a')
    for i in output:
        if '动态' in i:
            ip, mac, _ = i.strip().split()
            ls.append([ip, mac])
    return ls


if __name__ == '__main__':
    res = lan_ip_mac()
    res.append(local_ip_mac())
    print(res)

    # 结果写入文本
    txt = 'ip_mac.txt'
    out_txt = '\n'.join(['\t'.join(i) for i in res])
    with open(txt, 'w') as f:
        f.write(out_txt)

    msgbox(f'提取结果已保存到：{txt}')  # 注释掉此行则不弹窗提醒
"""

""" 扫描并输出
import os
import re
import threading

ips = []


def local_ip_mac():  # 本机IP和MAC
    output = os.popen('ipconfig /all')
    for i in output:
        if '物理地址.' in i:
            mac = i.split(':')[1].strip()
        if 'IPV4' in i.upper() and '(' in i:
            ip = i.split(':')[1].split('(')[0].strip()
    if ip and mac:
        return [ip, mac]


def ip_online(ip):  # 判断IP是否在线
    cmd = f'ping -n 1 {ip}'
    output = os.popen(cmd)
    if any('TTL' in i.upper() for i in output):
        ips.append(ip)


def ip2mac(ip):  # 通过IP查MAC
    loc_ip, mac = local_ip_mac()
    if ip == loc_ip:
        return mac
    cmd = f'arp -a {ip}'
    output = os.popen(cmd)
    outstr = ' '.join(list(output))
    if '未找到 ARP 项' not in outstr:  # 排除本机
        macs = re.findall('(([A-Fa-f0-9]{2}-){5}[A-Fa-f0-9]{2})', outstr, re.S)
        for i in macs[0]:
            if len(i) == 17:
                return i


def speed_up(func, args_list):  # 多线程
    thread_list = []
    for i in args_list:
        t = threading.Thread(target=func, args=(i,))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    t.join()


if __name__ == '__main__':
    print('扫描中，稍等片刻...')
    loc_ip, mac = local_ip_mac()
    ip_range = '.'.join(loc_ip.split('.')[:-1])  # 通过本机IP拼接IP段
    ip_list = [f'{ip_range}.{i + 1}' for i in range(255)]
    speed_up(ip_online, ip_list)  # 多线程扫描
    res = [(i, ip2mac(i)) for i in sorted(ips)]
    print('扫描结果：', sorted(res))
"""
