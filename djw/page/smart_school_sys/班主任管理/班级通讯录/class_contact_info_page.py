# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/22 10:48
@Author :李国彬
============================
"""
import time

import allure
from selenium.webdriver.common.by import By
from common.file_path import wait_file_down_and_clean

from common.base_page import BasePage


class ClassContactInfoPage(BasePage):
    """通讯录详情页面"""

    @allure.step("获取班级通讯录列表信息")
    def get_class_addr_book_detail_info(self):
        title = (By.XPATH, '//*[@role="tablist"]//*[contains(text(),"通讯录列表")]')
        name = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[3]//span/span')  # 姓名
        sex = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[4]//span/span')  # 性别
        phone = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[5]//span/span')  # 手机号
        group = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[6]//span/span')  # 所在小组
        duty = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[7]//span/span')  # 班级职务
        job = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[8]//span/span')  # 单位及职务
        self.wait_visibility_ele(title)
        dict_key = ("name", "sex", "phone", 'group', 'duty', 'job')
        dict_info = self.publish_get_info(name, sex, phone, group, duty, job, t=dict_key)
        return dict_info

    @allure.step('获取通讯录详情姓名信息')
    def get_contact_name(self, name):
        name_info = (By.CSS_SELECTOR, '[ctrl-id="xm"] [title]')
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(3)
        return self.find_elem(name_info).get_attribute('textContent')

    @allure.step('查询通讯录列表人员')
    def search_list_user(self, name=''):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('获取通讯录卡片人员姓名')
    def get_contact_card_names(self):
        names_ele = (By.CSS_SELECTOR, '[class="item-name"]')
        return [i.text for i in self.find_elms(names_ele)]

    @allure.step('下载班级通讯录')
    def download_contact(self, file_name):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name)
