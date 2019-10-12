'''
@author: lgx
@Email:297979949@qq.com
@project: logging
@file: logging_class.py
@time: 2019-09-26 9:45
@desc:本脚本实现把日志输出到文件中和控制台
'''
import logging
import sys

class rizhi:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # logger的日志等级一定要写
        self.logger.setLevel(level=logging.INFO)
        self.log_level=logging.INFO
        self.formatter=logging.Formatter('%(asctime)s--[%(levelname)s]: %(message)s')



    def send_to_file(self,file_path):
        """
        此方法实现了把日志保存到文件中
        :param file_path: 日志保存的位置
        :return:
        """

        #实例化FileHeadler对象
        file_headler=logging.FileHandler(file_path)
        #设置FileHeadler的日志等级
        file_headler.setLevel(level=self.log_level)
        #设置FileHeadler日志输出的格式
        file_headler.setFormatter(self.formatter)

        #把FileHeadler对象加入loggerzhong
        self.logger.addHandler(file_headler)


    def send_to_stdout(self):
        """
        使用StreamHeadler方法实现了把日志输出到标准输出
        :return:
        """

        # 实例化StreamHeadler对象
        stream_headler=logging.StreamHandler(sys.stdout)
        # 设置StreamHeadler的日志等级
        stream_headler.setLevel(self.log_level)
        # 设置StreamHeadler日志输出格式
        stream_headler.setFormatter(self.formatter)
        # 把StreamHeadler对象加入logging实例化对象logger中
        self.logger.addHandler(stream_headler)


    def log(self,message,log_value=20):
        """
        本方法实现输出不同类型的日志,默认info,不用传值
        :param message: 日志的内容
        :param type_value: 日志的类型
        :return:
        """
        if log_value == 20:
            self.logger.info(message)
        elif log_value == 30:
            self.logger.warning(message)
        elif log_value == 40:
            self.logger.error(message,exc_info=True)
        elif log_value == 50:
            self.logger.critical(message)


# p_file='test.log'
# mes="测试成功"
# v=int(20)
# rz=rizhi()
# rz.send_to_file(p_file)
# rz.send_to_stdout()
# rz.log_type(v,mes)



