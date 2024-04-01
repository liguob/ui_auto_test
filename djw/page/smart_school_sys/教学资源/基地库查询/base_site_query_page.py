# -*- coding: UTF-8 -*-
"""
Created on 2021年04月16日 

@author: liudongjie
"""
import allure
from selenium.webdriver.common.by import By

from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage


class BaseSiteQueryPage(EduSourcePage):
    """基地库查询主页"""

    @allure.step('查询基地')
    def search_base_site(self, name):
        self.locator_tag_search_input(placeholder='基地名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入基地详情')
    def go_base_site_detail(self, name):
        """进入详情，返回基地名称"""
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        site_name_ele = (By.CSS_SELECTOR, '[ctrl-id=name] [title]')
        return str(self.find_elem(site_name_ele).text).strip()
