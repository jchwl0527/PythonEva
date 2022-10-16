import requests


def send_wechat(msg):
    token = 'e4f4a98a3abd4c9cb3a848adfc2a13b9'
    title = '标题'
    content = msg
    template = 'html'
    url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
    print(url)
    r = requests.get(url=url)
    print(r.text)


if __name__ == '__main__':
    msg = '内容'
    send_wechat(msg)
