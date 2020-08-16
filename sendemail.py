import smtplib
from email.mime.text import MIMEText
import os
import time
def send_emil():


    sender = os.environ.get('Email_user') # 可以把邮件的账号和密码放到环境变量中，利用这个方式进行信息保密！
    # print(sender)
    sender_alias = 'chengchao<example@qq.com>' #名字不能用中文，否则邮箱显示为空白
    password = os.environ.get('Email_pass') # 可以把邮件的账号和密码放到环境变量中，利用这个方式进行信息保密！
    # print(password)
    reciver = ['email1','email2','email3']
    body = '<h1>python email</h1><p>python让生活更美好！</p>' #可以使用html格式写邮件正文
    msg = MIMEText(body,'html') #格式转换
    msg['subject'] = 'python 主题'
    msg['from']=sender_alias
    msg['to']=','.join(reciver)

    s=smtplib.SMTP_SSL(host,port)
    s.login(sender,password)
    s.sendmail(sender,reciver,msg.as_string())

def time_calc():
    while True:
        time.sleep(0.5)
        time_start=time.time()
        localtime = time.localtime(time_start)
        hour = localtime.tm_hour
        min = localtime.tm_min
        second = localtime.tm_sec
        year = localtime.tm_year
        mon = localtime.tm_mon
        day = localtime.tm_mday
        if min==51 and second ==0: # 每个小时的17分发一次，可以任意修改时间点
            send_emil()
            time.sleep(1)
            print(f'{year}—{mon}-{day}-{hour}点-{min}分：邮件已发送！')

if __name__=="__main__":
    host = 'smtp.qq.com'
    port = 465  # host和port可以查看qq邮箱的设置！
    time_calc()

