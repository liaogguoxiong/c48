'''
@author: lgx
@Email:297979949@qq.com
@project: c48
@file: query_service_status.py
@time: 2019-10-12 17:56
@desc:查询金税盘服务器状态
'''
from dzfp_c48 import *
from deal_input_file import *
from SEND_EMAIL import *



def main():
    service_status={}
    info=get_info()
    for ipp in info:
        cs=c48_sys(ipp)
        cs.login_c48()
        for i in info[ipp]:
            shuihao=i[0]
            name=i[1]
            status=cs.service_status(shuihao,name)
            service_status[name]=status

        cs.close_browse()

    """
    判断服务状态,如果不可用,则发送邮件报警
    """
    normal_value="可用"
    # 初始化邮箱设置
    mail_server = 'smtp.qq.com'
    mail_user = '297979949@qq.com'
    mail_passwd = 'rhoexjltojtcbghc'
    sender = '297979949@qq.com'
    receiver = '297979949@qq.com'



    sm=SEND_MAIL(mail_server,mail_user,mail_passwd,sender,receiver)

    for company_name in service_status:
        #print(company_name,service_status[company_name])
        if service_status[company_name] != normal_value:
            subject="{}的服务状态不正常".format(company_name)
            mes="{}的服务状态为:{}".format(company_name,service_status[company_name])
            rz.log(subject,30)
            rz.log(mes,30)
            sm.email_heading(subject)
            sm.send_text(mes,"plain")
            sm.send_mail()
            rz.log("邮件发送成功")





if __name__ == '__main__':
    main()