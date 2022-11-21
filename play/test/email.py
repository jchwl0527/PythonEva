# coding=utf-8
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

pwd = 'Ca5A6JnVYicpIeZ2'

# qq邮箱smtp服务器
host_server = 'smtp.88.com'
# sender_qq为发件人的qq号码
sender_qq = 'syr626@88.com'
# pwd为qq邮箱的授权码
pwd = pwd
# 发件人的邮箱
sender_qq_mail = 'syr626@88.com'
# 收件人邮箱
receiver = 'tntoppo@qq.com'
# 邮件的正文内容
mail_content = '登录邮箱发邮件的测试'
# 邮件标题
mail_title = '测试邮件'
# ssl登录
smtp = SMTP_SSL(host_server)
# set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)
# 邮件内容需要转MIMEText
msg = MIMEText(mail_content, "plain", 'utf-8')
# 邮件主题
msg["Subject"] = Header(mail_title, 'utf-8')
# 发件人
msg["From"] = sender_qq_mail
# 收邮件人
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
