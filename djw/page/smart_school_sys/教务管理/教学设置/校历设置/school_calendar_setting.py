"""
============================
Author:杨德义
============================
"""
import time

import allure
import random
from time import sleep
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.decorators import change_reset_implicit


class SchoolCalendarSetting(BasePage):
    """教务管理-教学设置-校历设置"""

    # 工作日单元格
    set_holiday_btn = (By.XPATH, '//*[@class="c_content_cell_bottom"]//ancestor::*[@class="c_content_cell"]')
    # 假日单元格
    cancel_holiday_btn = (By.CSS_SELECTOR, '.c_content_cell_holidaybg')
    # 年月下拉列表项
    month_year_item = (By.XPATH, '//*[@x-placement]//*[contains(@class, "el-select-dropdown__item")]//*[contains(text(), "{}")]')

    @property
    @change_reset_implicit()
    @allure.step('获取所有工作日单元格元素')
    def set_holiday_btns(self):
        return self.driver.find_elements(*self.set_holiday_btn)

    @property
    @change_reset_implicit()
    @allure.step('获取所有假日单元格元素')
    def cancel_holiday_btns(self):
        return self.driver.find_elements(*self.cancel_holiday_btn)

    @allure.step('随机双击某个工作日将其设为假日')
    def random_set_a_holiday(self):
        set_btns = self.set_holiday_btns
        if not set_btns:
            # 1、如无工作日, 则随机选一个假日双击设为工作日
            cancel_btns = self.cancel_holiday_btns
            cancel_btn = random.choice(cancel_btns)
            for _ in range(2):
                self.element_click(cancel_btn)
            sleep(0.5)
            self.explicit_wait_ele_lost(self.WEB_TIP)
            # 2、再双击设为假日
            set_btn = self.driver.find_element(*self.set_holiday_btn)
            for _ in range(2):
                self.element_click(set_btn)
        else:
            sleep(1)
            # 如有工作日, 则随机选一个双击设为假日
            set_holiday_btn = (By.XPATH, '(//*[@class="c_content_cell_bottom"]//ancestor::*[@class="c_content_cell"])[6]')
            ele = self.find_elem(set_holiday_btn)
            self.mouse_double_click(ele)
            self.move_and_move_to_click(loc1=set_holiday_btn, loc2=(By.XPATH, "(//*[contains(text(), '设为假日')])[6]"))
            # set_holiday_btn = (By.XPATH, '(//*[@class="c_content_cell_bottom"]//ancestor::*[@class="c_content_cell"])[1]')
            # workday = (By.XPATH, '(//*[@class="c_content_cell_bottom"]//*[contains(text(),"设为假日")])[1]')
            # self.move_and_move_to_click(loc1=set_holiday_btn, loc2=(By.XPATH, "//*[contains(text(), '设为假日')]"))
            # self.move_to_ele(set_holiday_btn)
            # self.element_click(workday)
        return self

    @allure.step('随机双击某个假日将其设为工作日')
    def random_cancel_a_holiday(self):
        cancel_btns = self.cancel_holiday_btns
        if not cancel_btns:
            # 1、 如无假日, 则随机选一个工作日双击设为假日
            set_btns = self.set_holiday_btns
            set_btn = random.choice(set_btns)
            for _ in range(2):
                self.excute_js_click_ele(set_btn)
            sleep(0.5)
            self.explicit_wait_ele_lost(self.WEB_TIP)
            # 2、 再双击设为工作日
            cancel_btn = self.driver.find_element(*self.cancel_holiday_btn)
            for _ in range(2):
                self.excute_js_click_ele(cancel_btn)
        else:
            # 如有假日, 则随机选一个双击设为工作日
            sleep(1)
            cancel_btn = (
            By.XPATH, '(//*[@class="c_content_cell_bottom_cancel"]//ancestor::*[@class="c_content_cell"])[1]')
            holiday = (By.XPATH, '(//*[@class="c_content_cell_bottom_cancel"]//*[contains(text(),"取消假日")])[1]')

            self.move_to_ele(cancel_btn)
            self.excute_js_click_ele(holiday)
        return self

    @allure.step('取消某月所有假日')
    def cancel_month_holidays(self):
        cancel_btns = self.driver.find_elements(*self.cancel_holiday_btn)
        while cancel_btns:
            self.mouse_double_click(cancel_btns[0])
            self.move_and_move_to_click(loc1=self.cancel_holiday_btn, loc2=(By.XPATH, "//*[contains(text(), '取消假日')]"))
            self.wait_success_tip()
            time.sleep(1)
            cancel_btns = self.driver.find_elements(*self.cancel_holiday_btn)
        return self

    @allure.step('选择月份')
    def select_month(self, month: str):
        """
        :param month: 1月-9月 10月-12月
        """
        expand_month_list = (By.CSS_SELECTOR, '[class$=top_month] input')
        self.poll_click(expand_month_list)
        self.excute_js_click_ele((self.month_year_item[0], self.month_year_item[1].format(month)))
        sleep(3)
        return self

    @allure.step('选择年份')
    def select_year(self, year: str):
        """
        :param year: xxxx
        """
        expand_year_list = (By.CSS_SELECTOR, '[class$=top_year] input')
        self.poll_click(expand_year_list)
        self.excute_js_click_ele((self.month_year_item[0], self.month_year_item[1].format(year)))
