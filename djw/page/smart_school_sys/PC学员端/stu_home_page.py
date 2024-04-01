# -*- coding: UTF-8 -*-
"""
Created on 2021年04月28日
@author: liudongjie
"""

import allure
from common.base_page import BasePage
from selenium.webdriver.common.by import By


class StudentHomePage(BasePage):
    # 培训记录按钮位置
    training_records_button_loctor = (By.XPATH, '//span[text()="培训记录"]')
    # 教学评价按钮位置
    teaching_evaluation_button_loctor = (By.XPATH, '//span[text()="教学评价"]')
    # 待办菜单
    wait_deal = (By.XPATH, '//div[@class="ds-home-tab-panel ds-home-tab-panel-one"]/div/div/div/div[@ac="true"]')
    # 作业提交
    bsub_button_loctor = (By.XPATH, '//div[@title="作业提交"]')

    def training_records_button_click(self):
        """
        点击培训记录,进行培训记录页面
        """
        self.element_click(loc=self.training_records_button_loctor)
        from djw.page.smart_school_sys.PC学员端.培训记录.training_records_page import TrainingRecordsPage
        return TrainingRecordsPage(self.driver)

    def teaching_evaluation_button_click(self):
        """
        点击教学评价,进行教学评价页面
        """
        self.element_click(loc=self.teaching_evaluation_button_loctor)
        from djw.page.smart_school_sys.PC学员端.教学评价.teaching_evaluation_page import TeachingEvaluationPage
        return TeachingEvaluationPage(self.driver)

    def goto_undone(self):
        """"点击待办,进入待办页面"""
        self.excute_js_click(self.wait_deal)
        from djw.page.smart_school_sys.PC学员端.首页.待办.wait_done import WaitDone
        return WaitDone(self.driver)

    def go_bsub_page_click(self):
        """进入到作业提交页面"""
        self.find_elem(loc=self.bsub_button_loctor).click()
        from djw.page.smart_school_sys.PC学员端.首页.作业提交.bsub_page import BsubPage
        return BsubPage(self.driver)

    @allure.step("进入退学管理")
    def go_stu_drop_manage(self):
        from djw.page.smart_school_sys.PC学员端.退学管理.stu_drop_manage_page import StuDropManagePage
        self.element_click(StuDropManagePage.menu_drop_manage)
        return StuDropManagePage(self.driver)
