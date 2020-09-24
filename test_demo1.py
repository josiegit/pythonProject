# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import shelve
"""
先获取cookies并保存，记得把旧cookies.dat等文件删除
"""
class TestDemoa():
    def setup_method(self,method):
        options=Options()
        options.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome()
        self.var={}

    def teardown_method(self,method):
        self.driver.quit()

    def test_demoa(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db=shelve.open("cookies")
        # db['cookie']=self.driver.get_cookies()
        cookies=db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_link_text("通讯录").click()
        sleep(3)
        db.close()