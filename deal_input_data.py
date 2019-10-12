'''
@author: lgx
@Email:297979949@qq.com
@project: export_data
@file: deal_input_data.py
@time: 2019-10-10 16:32
@desc:处理文本中的数据,形成所需的格式
'''

import re

def deal_method():

    file="input_file"
    """
    读出文件,readlines()
    读出所有行,形成列表
    """
    with open(file,"r",encoding="utf-8") as f:
        r=f.readlines()

    res=[]  # 用于存放去掉-的数据
    dic={}  # 利用字典的唯一性,去掉相同的ip地址

    for i in r:
        if i != "\n":       #去掉输入文件多余的空行
            r_l=i.split()   #把换行符去掉
            # print(r_l)
            l=re.split("-",r_l[0])  #r_l是一个字段,r_l[0]取出其值

            """
            把ip地址作为key值,加入空字典中,
            由于唯一性,相同的ip地址会被去掉
            """
            dic[l[0]]="1"
            res.append(l)

    # print(len(res))

    d1={}   #用于存放key值为ip地址,value为由税号和分机号组成的字典

    """
    遍历key为ip地址的字典,
    如果列表中有此ip,则此ip作为key
    列表中的其他值为value
    """
    for k in dic:

        for j in res:
            if k in j:
                d1.setdefault(k,[]).append(j[1:])   #用setdefault()方法来创建value为列表的字典


    return d1










# deal_method()