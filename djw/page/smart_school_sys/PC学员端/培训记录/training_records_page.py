# -*- coding: UTF-8 -*-
"""
Created on 2021年04月28日 

@author: liudongjie
"""

from common.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class TrainingRecordsPage(BasePage):

    top_floor_iframe = (By.XPATH, '//iframe')
    # 培训记录的iframe
    training_records_tbody_loctor = (By.XPATH, '//tbody[@handler="datagrid_body_tobdy"]')
    # 培训记录列表位置

    def go_raining_records_iframe(self):
        """
        进入顶层iframe
        """
        self.switch_to_frame(loc=self.top_floor_iframe)

    def operation_training_records_tbody(self, row, value):
        """
        操作培训记录列表
        """
        tbody = self.find_elem(loc=self.training_records_tbody_loctor)
        tr_list = tbody.find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            div_list = td_list[2].find_elements_by_xpath('.//div')
            if div_list[3].text == value:
                a_list = td_list[row].find_elements_by_xpath('.//a')
                a_list[0].click()
                break
        sleep(1)
