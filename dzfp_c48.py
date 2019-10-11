'''
@author: lgx
@Email:297979949@qq.com
@project: export_data
@file: dzfp_c48.py
@time: 2019-10-10 9:31
@desc:实现电子发票管理平台的各项功能
'''

from selenium import webdriver
import time,datetime
from  PIL import Image
from recognize_verify_code import *
from selenium.webdriver.support.select import Select
from deal_input_data import *

class c48_sys():

    def __init__(self,ipp):
        """
        :param ipp:ip加端口号
        """
        # self.chrome_options=webdriver.ChromeOptions()
        # self.chrome_options.add_argument("headless")
        self.driver = webdriver.Chrome()   # 实例化selenium.webdriver
        self.ipp=ipp
        self.login_url='http://{}/zzs_kpfw_manager/login.htm'.format(ipp)   #c48登录的url
        self.base_url='http://{}/zzs_kpfw_manager'.format(ipp)  #跳转到其他功能的基础url

    def login_c48(self):
        """
        实现登录c48的功能,识别验证码
        :return: 0 表示登录成功
        """
        login_screen_path = "C:/2/screen.png"   # 存c48登录界面的截图位置
        verify_code_path="C:/2/verfy_code.png"  # 保存验证码的图片的位置

        self.driver.get(self.login_url)
        self.driver.implicitly_wait(8)  # 隐形等待8秒,等待浏览器加载完
        self.driver.maximize_window()   # 浏览器窗口最大化


        """
        死循环,不停滴识别验证码
        直到识别登录成功
        """
        while True:

            self.driver.save_screenshot(login_screen_path)  # 截取整个浏览器的图片,并保存起来
            location = self.driver.find_element_by_id("gencode").location   # 取验证码的位置信息
            size = self.driver.find_element_by_id("gencode").size   # 获取验证码的大小


            """
            根据验证码的大小和在整个登录界面
            截图的位置来裁剪出验证码
            
            注意:#坑爹,电脑分辨率为100%的时候才能够正确截取,其他大小的时候无法正确截取
            
            
            """
            coordinate = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                          int(location['y'] + size['height']))

            im = Image.open(login_screen_path)

            im_1 = im.crop(coordinate)  # 裁剪验证码

            im_1.save(verify_code_path) # 保存截取成功的验证码


            """
            传入保存验证码图片的位置,
            调用recognize_code()进行验证码识别
            返回识别的验证码,code为字符串类型
            """
            code=recognize_code(verify_code_path)
            print("识别出的验证码:",code)

            """
            由于识别的效率太低,code经常为
            None,当为None时就是识别不到,
            重新刷新网页,再次获取验证码
            """
            if code == None:
                time.sleep(1)
                self.driver.refresh()
                continue


            """
            识别到验证码之后,
            输入账号密码验证码
            提交登录
            """
            self.driver.find_element_by_id("user_account").send_keys("admin")   # 输入账号
            time.sleep(1)
            self.driver.find_element_by_id("password").send_keys("Aisino123+")  # 输入密码
            time.sleep(1)
            self.driver.find_element_by_id("validCode").send_keys(code) # 输入验证码
            time.sleep(1)
            self.driver.find_element_by_class_name("button_login").click()  # 点击登录按钮
            time.sleep(3)

            """
            由于验证码不一定识别成功,
            我们就得需要判断此时在不在登录成功之后的页面
            登录成功之后的页面的源代码有[欢迎您，系统管理员]
            我们可以根据此来做判断
            如果成功的话,返回0
            失败的话,重新请求登录页面的url
            
            注意:本来是想登录失败之后,重新刷新网页记性了,但是
            验证码的框会显示出东西挡住了截图
            """
            word="欢迎您，系统管理员"

            if word in self.driver.page_source:
                print("登录成功")
                time.sleep(3)
                return 0

            else:
                print("验证码不正确")
                time.sleep(2)
                self.driver.get(self.login_url)



    def huizong_fp(self,shuihao,fj_num):
        """
        实现月度统计的功能
        :param shuihao:公司的税号
        :param fj_num:金税盘的分机号
        :return:
        """

        url="/tax/monthly_statistics/list.htm"   # c48的功能url都是通过基本的url加上专属的url组合而成
        huizong_url=self.base_url+url
        year = datetime.datetime.now().year     # 年份
        mon = datetime.datetime.now().month    # 月份
        """
        由于月度汇总都是汇总上个月的,
        1月份导的是12月份的
        """
        if mon == 1:
            mon = 12

        self.driver.get(huizong_url)
        self.driver.implicitly_wait(8)
        time.sleep(1)
        """
        传入税号,公司名称会根据税号带出
        """
        self.driver.find_element_by_xpath("//input[@id='_easyui_textbox_input4']").send_keys(shuihao)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='_easyui_textbox_input6']").send_keys(fj_num)    # 传入分机号
        time.sleep(1)
        self.driver.find_element_by_id("search_year").send_keys(year)   # 传入年份
        time.sleep(1)
        self.driver.find_element_by_id("search_month").send_keys(mon-1) # 传入月份
        time.sleep(1)
        """
        发票种类是个下拉标签select,
        使用Select方法来选择
        """
        Select(self.driver.find_element_by_name("search_fpzl")).select_by_value("51")
        time.sleep(1)
        self.driver.find_element_by_id("queryInfo").click()     # 点击查询按钮
        time.sleep(2)
        self.driver.find_element_by_id("doExportBntPdf").click()    #点击导出pdf按钮



    def close_browse(self):
        time.sleep(3)
        self.driver.close()

# ipp="192.168.20.212:8081"
# shuihao="911100000828144374"
# fjh="1"

info=deal_method()
print(info)
n=0
for ipp in info:
    cs=c48_sys(ipp)
    value=cs.login_c48()
    if value == 0:
        for i in info[ipp]:
            shuihao=i[0]
            fjh=i[1]
            cs.huizong_fp(shuihao,fjh)
            n+=1
    cs.close_browse()

print(n)












