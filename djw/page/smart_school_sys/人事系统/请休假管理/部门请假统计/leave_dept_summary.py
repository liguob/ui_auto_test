"""
============================
Author:杨德义
============================
"""
import allure
import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.file_path import wait_file_down_and_clean


class LeaveDeptSummary(BasePage):
    """部门请假统计页面类"""

    # 进入部门/人员选择
    datachoice_input = (By.CSS_SELECTOR, '.ldl_head_btn .ds-datachoice-input')
    # 部门/人员检索框
    search_input = (By.CSS_SELECTOR, '.el-input__inner[placeholder=输入关键字进行过滤]')
    # 部门/人员检索按钮
    search_btn = (By.CSS_SELECTOR, '.icon-Magnifier')
    # 部门/人员统计页导出按钮
    export_btn = (By.CSS_SELECTOR, '.ldl_head_btn [vi-f=exportBtn]')
    # 省委党校人员
    leave_account = (By.XPATH, '//*[contains(@class, "expanded")]//following-sibling::*[text()=" 省委党校 "]/..//following-sibling::*[@role="group"]//*[text()=" 教研部请假测试账户 "]')
    # 省委党校部门
    party_dept = (By.XPATH, '//*[contains(@class, "expanded")]//following-sibling::*[text()=" 省委党校 "]/..//following-sibling::*[@role="group"]//*[text()=" {} "]')
    # 部门/人员选择确定按钮
    confirm = (By.XPATH, '//*[text()="确定"]/..')

    @allure.step('部门选择')
    def select_dept(self, dept_name='教研部'):
        self.poll_click(self.datachoice_input)
        dept = self.explicit_wait_ele_presence((self.party_dept[0], self.party_dept[1].format(dept_name)))  # 等待四川省委党校查询部门加载
        self.clear_then_input(self.search_input, dept_name)
        self.poll_click(self.search_btn)
        time.sleep(0.5)
        self.poll_click(dept)  # 点击四川省委党校查询部门
        time.sleep(0.5)
        self.poll_click(self.confirm)
        time.sleep(1)
        return self

    @property
    @allure.step('判断是否暂无(统计)数据')
    def is_summary_empty(self):
        """页面暂无数据->返回True, 页面有数据->返回False"""
        empty_loc = (By.XPATH, '//*[@class="el-table__empty-text" and contains(text(), "暂无数据")]')
        return self.is_element_exist(empty_loc)

    @allure.step('人员选择')
    def select_person(self, person_name):
        self.poll_click(self.datachoice_input)
        person = self.explicit_wait_ele_presence((self.leave_account[0], self.leave_account[1].format(person_name)))  # 等待省委党校查询账户加载
        self.clear_then_input(self.search_input, person_name)
        self.poll_click(self.search_btn)
        time.sleep(0.5)
        self.poll_click(person)  # 点击省委党校查询账户
        time.sleep(0.5)
        self.poll_click(self.confirm)
        time.sleep(1)
        return self

    @property
    @allure.step('指定部门请假统计数据')
    def dept_summary_data(self):
        items = (By.XPATH, '//div[contains(@class,"scrolling")]//tr/td[{}]')
        locators = list(map(lambda x: (items[0], items[1].format(x)), range(5, 11)))
        title = ('事假', '病假', '婚假', '产假', '丧假', '年假')
        return self.publish_get_info(*locators, head=title)

    @property
    @allure.step('指定人员请假统计数据')
    def person_summary_data(self):
        items = (By.XPATH, '//div[contains(@class,"scrolling")]//tr/td[{}]')
        locators = list(map(lambda x: (items[0], items[1].format(x)), range(4, 10)))
        title = ('事假', '病假', '婚假', '产假', '丧假', '年假')
        return self.publish_get_info(*locators, head=title)

    @allure.step('部门/人员请假统计导出')
    def export_leave_summary(self):
        self.poll_click(self.export_btn)
        return wait_file_down_and_clean('请假统计.xls')
