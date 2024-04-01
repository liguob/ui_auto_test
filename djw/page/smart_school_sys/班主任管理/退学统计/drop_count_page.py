# encoding=utf-8
import time
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage
import json


class DropCountPage(BasePage):
    """退学统计"""
    menu_drop_count = (By.XPATH, '//span[contains(text(), "退学统计")]/parent::div')

    @allure.step("搜索班级")
    def search_class_drop_count(self, class_name):
        input_search = (By.XPATH, '//div[@class="search-input el-input"]/input')  # 班次搜索框
        self.clear_then_input(input_search, class_name+'\n')
        time.sleep(1)
        return self

    @allure.step("搜索学员")
    def search_stu_drop_count(self, stu_name):
        input_search = (By.XPATH, '//label[contains(text(), "退学学员列表")]//ancestor::div[@class="ds-panel-header"]//div[@class="search-input el-input"]/input')
        self.clear_then_input(input_search, stu_name+'\n')
        time.sleep(1)
        return self

    @property
    @allure.step('获取指定班次退学人数')
    def drop_count(self):
        loc = (By.XPATH, '(//div[contains(@class,"is-scrolling")]//td[5]/div/div)[1]')
        return json.loads(self.trim_text(loc))

    @property
    @allure.step('获取指定班次实际人数')
    def actual_count(self):
        loc = (By.XPATH, '(//div[contains(@class,"is-scrolling")]//td[4]/div/span)[1]')
        return json.loads(self.trim_text(loc))

    @allure.step("点击退学人数的超链接")
    def click_drop_num(self):
        time.sleep(1.5)
        drop_num = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[5]/div/div')
        self.element_click(drop_num)
        return self

    @allure.step("获取班级列表信息")
    def get_drop_class_list_info(self):
        class_name = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[2]')  # 班次名称
        train_date = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[3]')  # 培训时间
        actual_num = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[4]')  # 实际人数
        drop_num = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[5]')  # 退学人数
        title = ("class_name", "train_date", "actual_num", "drop_num")
        info = self.publish_get_info(class_name, train_date, actual_num, drop_num, t=title)
        return info

    @allure.step("获取退学学员列表信息")
    def get_drop_stu_list_info(self):
        time.sleep(0.5)
        text_name = (By.XPATH, '//label[text()=" 退学学员列表 "]/ancestor::div[@class="ds-page-center"]//div[contains(@class,"is-scrolling")]//td[2]')  # 学员姓名
        text_date = (By.XPATH, '//label[text()=" 退学学员列表 "]/ancestor::div[@class="ds-page-center"]//div[contains(@class,"is-scrolling")]//td[3]')  # 退学时间
        text_reason = (By.XPATH, '//label[text()=" 退学学员列表 "]/ancestor::div[@class="ds-page-center"]//div[contains(@class,"is-scrolling")]//td[4]')  # 退学事由
        title = ("name", "date", "reason")
        info = self.publish_get_info(text_name, text_date, text_reason, t=title)
        return info
