# -*- coding: UTF-8 -*-
"""
Created on 2021年05月20日
@author: liudongjie
"""

from common.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class BsubPage(BasePage):

    search_task_send_loctor = (By.XPATH, '//input[@placeholder="作业名称"]')
    # 作业搜索框输入位置
    search_task_button_loctor = (By.XPATH, '//button[@class="search-button"]')
    # 作业搜索框按钮位置

    def search_task_name(self, value):
        """搜索作业"""
        self.find_elem(loc=self.search_task_send_loctor).send_keys(value)
        self.find_elem(loc=self.search_task_button_loctor).click()
        sleep(1)

    def get_task_list_text(self, line, row):
        """获取作业列表某行某列的文本"""
        tbody = self.find_elem(loc=(By.XPATH, '//tbody'))
        tr_list = tbody.find_elements_by_tag_name('tr')
        td_list = tr_list[line-1].find_elements_by_tag_name('td')
        if row == 5:
            a = td_list[row-1].find_element_by_xpath(".//a")
            return a.text
        else:
            span_list = td_list[row-1].find_elements_by_xpath('.//span')
            return span_list[1].text

    def get_upload_task_name(self):
        """获取作业列表中可以上传作业的作业名并返回一个列表"""
        task_list = []
        tbody = self.find_elem(loc=(By.XPATH, '//tbody'))
        tr_list = tbody.find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            name_list = td_list[1].find_elements_by_xpath('.//span')
            state_list = td_list[2].find_elements_by_xpath('.//span')
            time = td_list[3].find_element_by_xpath('.//font')
            if '剩余' in time.text and state_list[1].text == '待提交':
                task_list.append(name_list[1].text)
        return task_list

    def option_task_list(self, line, option):
        """对作业列表进行操作"""
        tbody = self.find_elem(loc=(By.XPATH, '//tbody'))
        tr_list = tbody.find_elements_by_tag_name('tr')
        td_list = tr_list[line-1].find_elements_by_tag_name('td')
        if option == '下载':
            a = td_list[4].find_element_by_xpath('.//a')
            a.click()
            sleep(3)
        elif option == '详情':
            a_list = td_list[7].find_elements_by_xpath('.//a')
            self.driver.execute_script("arguments[0].click();", a_list[0])
            sleep(1)
        elif option == '上传':
            a_list = td_list[7].find_elements_by_xpath('.//a')
            self.driver.execute_script("arguments[0].click();", a_list[1])
            sleep(1)

    def upload_file(self, file):
        """
        上传文件,并点击esc按钮
        """
        self.find_elem((By.XPATH, '//input[@name="file"]')).send_keys(file)
        from pykeyboard import PyKeyboard
        sleep(2)
        pyk = PyKeyboard()
        pyk.tap_key(pyk.cancel_key, 1)

    def get_task_details_text(self, line):
        """获取作业详情文本"""
        self.switch_to_handle(-1)
        tbody = self.find_elem(loc=(By.XPATH, '//tbody'))
        tr_list = tbody.find_elements_by_tag_name('tr')
        td = tr_list[line-1].find_element_by_tag_name('td')
        span_list = td.find_elements_by_xpath('.//span')
        return span_list[1].text

    def get_task_name(self):
        """获取作业列表中的作业名并返回一个列表"""
        task_list = []
        tbody = self.find_elem(loc=(By.XPATH, '//tbody'))
        tr_list = tbody.find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            name_list = td_list[1].find_elements_by_xpath('.//span')
            task_list.append(name_list[1].text)
        return task_list

    def get_download_task_name(self):
        """获取作业列表中上传了文件的作业名并返回一个列表"""
        task_list = []
        tbody = self.find_elem(loc=(By.XPATH, '//tbody'))
        tr_list = tbody.find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            name_list = td_list[1].find_elements_by_xpath('.//span')
            state_list = td_list[2].find_elements_by_xpath('.//span')
            if state_list[1].text != '待提交':
                task_list.append(name_list[1].text)
        return task_list



