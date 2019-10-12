'''
@author: lgx
@Email:297979949@qq.com
@project: export_data
@file: debug.py
@time: 2019-10-10 17:35
@desc:
'''

import os

f_path="C:/Users/lgx/Downloads"
file_list=os.listdir(f_path)
exist=0
for name in file_list:
    if "9144030097935050X1F" in name:
        print("在")
        exist=1

if exist !=1:
    print("不在")