'''
@author: lgx
@Email:297979949@qq.com
@project: c48
@file: main_process.py
@time: 2019-10-12 11:08
@desc:
'''
from dzfp_c48 import *
from deal_input_data import *
from logging_class import *



def main():



    info = deal_method()    # 处理输入文件的格式

    for ipp in info:
        if len(info[ipp][0]) != 2:
            user=info[ipp][0][2]
            passwd=info[ipp][0][3]
            cs = c48_sys(ipp,uname=user,passwd=passwd)
        else:
            cs=c48_sys(ipp)
        value = cs.login_c48()
        if value == 0:
            for i in info[ipp]:
                shuihao = i[0]
                fjh = i[1]
                cs.huizong_fp(shuihao, fjh)
                rz.log("\n\n\n")

        cs.close_browse()
if __name__ == '__main__':

    main()