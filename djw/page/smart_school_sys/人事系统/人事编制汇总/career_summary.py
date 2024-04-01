"""
============================
Author:杨德义
============================
"""
import allure
import json
from common.base_page import BasePage
from selenium.webdriver.common.by import By


class CareerSummary(BasePage):
    """人事事业编制汇总"""

    @allure.step('切至指定事业tab页')
    def switch_tab(self, tab_name):
        """tab_name:事业管理/事业专技/事业工勤"""
        self.locator_switch_tag(tag_name=tab_name, times=1)
        return self

    @allure.step('事业管理/事业专技/事业工勤相应等级实配数文本')
    def career_real_num(self, level):
        real_num = (By.XPATH,
                    f'//*[contains(@class, "is-scrolling")]//*[contains(@class, "post_rank_text__value") and @title="{level}"]'
                    f'//ancestor::td//following-sibling::*//*[contains(@class, "summarydb_real_num__value")]')
        return json.loads(self.get_ele_attribute(self.driver.find_element(*real_num), 'title'))

    @allure.step('事业管理/事业专技/事业工勤相应等级空缺数文本')
    def career_vacancy_num(self, level):
        vacancy_num = (By.XPATH,
                       f'//*[contains(@class, "is-scrolling")]//*[contains(@class, "post_rank_text__value") and @title="{level}"]'
                       f'//ancestor::td//following-sibling::*//*[contains(@class, "summarydb_left_num__value")]')
        return json.loads(self.get_ele_attribute(self.driver.find_element(*vacancy_num), 'title'))
