
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'


# 路径配置
import os

config_path=os.path.abspath(__file__)#当前文件的绝对路径
conf_path=os.path.dirname(config_path)#所在文件夹的路径
project_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据文件目录
data_path=os.path.join(project_path,'data')
data_file=os.path.join(project_path,'data','data.xlsx')
report_path=os.path.join(project_path,'report')
report_file=os.path.join(project_path,'report','report.html')
testcase_path=os.path.join(project_path,'testcase')

# 日志文件的根目录
log_file=os.path.join(project_path,'log','log.txt')



# log配置
import logging
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a"
                    )


# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'ivan-me@163.com'
smtp_password="hanzhichao123"

receiver="296170764@qq.com"
subject="接口测试报告"
body='hi,all,\n附件是接口测试报告，请查收。'

is_send_report=False


if __name__=="__main__":
    logging.info("hello,world")
    logging.info("中文日志")
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(data_path)
    print(data_file)




