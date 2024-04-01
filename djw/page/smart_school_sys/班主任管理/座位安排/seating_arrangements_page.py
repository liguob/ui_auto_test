# -*- coding: UTF-8 -*-
"""
Created on 2021年05月17日
@author: liudongjie
"""
import time

import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class SeatingArrangementsPage(HomePage):
    """座位安排管理页面"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入班次座位设置')
    def go_class_seats_set(self, name):
        self.locator_view_button(button_title='座位设置', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.班主任管理.座位安排.座位设置.class_seats_set_page import ClassSeatsSetPage
        time.sleep(4)
        return ClassSeatsSetPage(self.driver)
