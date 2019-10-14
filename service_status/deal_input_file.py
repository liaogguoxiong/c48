'''
@author: lgx
@Email:297979949@qq.com
@project: c48
@file: deal_input_file.py
@time: 2019-10-13 21:39
@desc:处理输入数据的格式
'''

import re

def get_info():
    """
    处理输入文件的格式,
    返回元素为税号的列表
    :return: 元素为税号的列表
    """
    f_path="D:/python_project/c48/service_status/guande"

    with open(f_path, "r", encoding="utf-8") as f:
        res = f.readlines()

    info= []        # 用于存放以ipp(ip和端口),公司名,税号组成的列表的列表
    ip_port={}
    for i in res:
        if i != "\n":
            i = i.strip()
            i = re.split("-",i)
            ipp=i[0]
            ip_port[ipp]="1"
            info.append(i)
    # print(info)
    # print(ip_port)

    """
    遍历key为ip地址的字典,
    如果列表中有此ip,则此ip作为key
    列表中的其他值为value

    """

    company_info={}
    for d in ip_port:
        for j in  info:
            if d in j:
                company_info.setdefault(d,[]).append(j[1:])

    # print(company_info)
    return  company_info





get_info()

