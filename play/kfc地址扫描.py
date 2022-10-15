import csv

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

f = open('kfc.csv', mode='a', encoding='utf-8', newline='')
# 表头
csv_writer = csv.DictWriter(f, fieldnames=[
    '餐厅名称',
    '餐厅地址',
    '详情',
])

# 表单数据
for i in range(1, 11):
    data = {
        'cname': '',
        'pid': '',
        'keyword': '河南',
        'pageIndex': f'{i}',
        'pageSize': '10',
    }
    # 请求字符串
    params = {'op': 'keyword'}

    response = requests.post(url=url, params=params, headers=headers, data=data)
    json_data = response.json()  # 将结果进行反序列化 将对象转化为可以传输、储存的数据

    for i in json_data['Table1']:
        name = i['storeName']
        address = i['addressDetail']
        services = i['pro']
        print(name, address, services)

        dict = {
            '餐厅名称': name + '餐厅',
            '餐厅地址': address,
            '详情': services
        }
        csv_writer.writerow(dict)

# import requests
#
# url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
#
#
# def page_number(names):
#     data = {
#         'cname': '',
#         'pid': '',
#         'keyword': names,
#         'pageIndex': '1',
#         'pageSize': '10',
#     }
#     response = requests.post(url=url, headers=headers, data=data)
#     json_data = response.json()
#     number = json_data['Table'][0]['rowcount']
#     return number
#
#
# def parse_json(name):
#     number1 = page_number(name)
#     for i in range(1, number1 + 1):
#         data = {
#             'cname': '',
#             'pid': '',
#             'keyword': name,
#             'pageIndex': str(i),
#             'pageSize': '10',
#         }
#         response = requests.post(url=url, headers=headers, data=data)
#         json_data = response.json()
#         for p in json_data['Table1']:
#             canteen = p['storeName']
#             address = p['addressDetail']
#             pro = p['pro']
#             print(canteen, address, pro)
#
#
# parse_json('大连')
