'''
@author: lgx
@Email:297979949@qq.com
@project: send_mail
@file: SEND_EMAIL.py
@time: 2019-09-06 11:12
@desc:
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SEND_MAIL:

    def __init__(self,mail_server,mail_user,mail_passwd,sender,receiver):
        '''
        # 初始化收件人,发件人,发送人的账号和授权密码
        :param mail_server: 邮件服务器
        :param mail_user: 邮件服务器的用户
        :param mail_passwd: 邮件服务器的授权码
        :param sender: 发件人
        :param receiver: 收件人
        '''
        self.mail_server = mail_server
        self.mail_user = mail_user
        self.mail_passwd = mail_passwd
        self.sender = sender
        self.receiver = receiver

        # 构建邮件对象Multipart对象
        self.msg=MIMEMultipart('mixed')


    def email_heading(self,subject):
        '''
        构建主题，发件人，收件人，日期是显示在邮件页面上的。
        :param subject: 传入邮件的主题
        :return:
        '''

        self.msg['From'] = Header(self.sender, 'utf-8').encode()
        self.msg['To'] = Header(self.receiver, 'utf-8').encode()
        self.msg['Subject'] = Header(subject, 'utf-8').encode()


    def send_text(self,text,type):
        '''
        发送文本邮件,传入的参数为邮件内容和文本类型
        :param text: 传入邮件内容正文
        :param type: 正文的类型,文本为plain,网页为html
        :return:
        '''
        mail_content = MIMEText(text, type, 'utf-8')
        self.msg.attach(mail_content)


    def send_image(self,pic_path):
        '''
        构建邮件附件图片
        :param pic_path: 传入图片的绝对路径
        :return:
        '''
        picture=open(pic_path,'rb').read()
        mail_image=MIMEImage(picture)
        mail_image.add_header('Content-ID', '<image1>')
        mail_image.add_header('Content-Disposition', 'attachment', filename=Header(pic_path, 'utf-8').encode())
        self.msg.attach(mail_image)


    def send_mail(self):
        '''
        发送邮件
        :return:
        '''
        smtp = smtplib.SMTP()
        smtp.connect(self.mail_server, 25)
        smtp.login(self.mail_user, self.mail_passwd)
        smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
        smtp.quit()