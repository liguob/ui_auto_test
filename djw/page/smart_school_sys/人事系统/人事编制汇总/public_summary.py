"""
============================
Author:杨德义
============================
"""
import allure
from common.base_page import BasePage
from selenium.webdriver.common.by import By
import json


class PublicSummary(BasePage):
    """人事参公编制汇总"""

    @allure.step('切至领导职数页')
    def switch_leader_tab(self):
        self.locator_switch_tag(tag_name='领导职数', times=1)
        return self

    @allure.step('切至职级职数页')
    def switch_duty_tab(self):
        self.locator_switch_tag(tag_name='职级职数', times=1)
        return self

    @allure.step('领导职数相应等级实配数文本')
    def leader_real_num(self, level):
        loc = (By.XPATH,
         f'//*[contains(@class, "is-scrolling")]//*[contains(@class, "leader_leaderdb_civil_rank_text__value") and @title="{level}"]'
         f'//ancestor::td//following-sibling::*//*[contains(@class, "leader_leaderdb_real_num__value")]')
        return json.loads(self.get_ele_attribute(self.driver.find_element(*loc), 'title'))

    @allure.step('领导职数相应等级空缺数文本')
    def leader_vacancy_num(self, level):
        loc = (By.XPATH,
         f'//*[contains(@class, "is-scrolling")]//*[contains(@class, "leader_leaderdb_civil_rank_text__value") and @title="{level}"]'
         f'//ancestor::td//following-sibling::*//*[contains(@class, "leader_leaderdb_left_num__value")]')
        return json.loads(self.get_ele_attribute(self.driver.find_element(*loc), 'title'))

    @allure.step('职级职数相应等级实配数文本')
    def duty_real_num(self, level):
        loc = (By.XPATH,
         f'//*[contains(@class, "is-scrolling")]//*[contains(@class, "postrank_rankdb_post_rank_text__value") and @title="{level}"]'
         f'//ancestor::td//following-sibling::*//*[contains(@class, "postrank_rankdb_real_num__value")]')
        return json.loads(self.get_ele_attribute(self.driver.find_element(*loc), 'title'))

    @allure.step('职级职数相应等级空缺数文本')
    def duty_vacancy_num(self, level):
        loc = (By.XPATH,
         f'//*[contains(@class, "is-scrolling")]//*[contains(@class, "postrank_rankdb_post_rank_text__value") and @title="{level}"]'
         f'//ancestor::td//following-sibling::*//*[contains(@class, "postrank_rankdb_left_num__value")]')
        return json.loads(self.get_ele_attribute(self.driver.find_element(*loc), 'title'))
