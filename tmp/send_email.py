
import  smtplib #连接smtp服务器并发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1.组装邮件正文
msg=MIMEMultipart()#混合格式消息体
body=MIMEText('python发送的邮件','plain','utf-8')#plain纯文字html
msg.attach(body)#将正文添加到msg对象中

# 2.组装邮件头
msg['From']='test_results@sina.com'
msg['To']='296170764@qq.com'
msg['Subject']="from python"

#4.附件
with open("../report/report.html","rb") as f:
    att_file=f.read()
att=MIMEText(att_file,'base64','utf-8')
att["content-Type"]='application/octet-stream'# 声明附件的内容格式 MIME数据流格式
att["content-Disposition"]='attachment;filename="report.html"'# 附件描述信息 filename是附件显示的文件名
msg.attach(att)# 将附件添加到消息对象中

# 3.连接smtp服务器并发送
smtp=smtplib.SMTP_SSL("smtp.sina.com")#建立连接
smtp.login("test_results@sina.com","hanzhichao123")#登录邮箱
smtp.sendmail("test_results@sina.com",
              "296170764@qq.com",
              msg.as_string())#将MIME格式邮件转成字符串发送
