'''
@author: lgx
@Email:297979949@qq.com
@project: c48
@file: export_month_summary.py
@time: 2019-10-12 11:08
@desc:导出月度统计
'''
import sys
sys.path.append("..")
from lib.dzfp_c48 import *
from deal_input_data import *


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