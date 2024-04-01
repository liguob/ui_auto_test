# -*- coding: UTF-8 -*-
"""
Created on 2021年09月06日
@author: liudongjie
"""
import time

import allure
from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage


class FirstAndBestPage(EduSourcePage):
    """评先评优页面类"""

    @allure.step('查询评先评优')
    def search_info(self, name):
        self.locator_search_input(placeholder="部门/姓名", value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('删除评先评优')
    def del_info(self, value):
        self.locator_view_button(button_title='删除', id_value=value)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('编辑评先评优')
    def edit_info(self, name, data: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)  # 等待编辑界面的数据加载
        from djw.page.smart_school_sys.人事系统.评先评优.best_info_page import BestInfoPage
        BestInfoPage(self.driver).edit_info(data)
        self.wait_success_tip()
        self.close_current_browser()
        self.switch_to_window(-1)
        return self

    @allure.step('新增评先评优')
    def add_info(self, data: dict):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.评先评优.best_info_page import BestInfoPage
        BestInfoPage(self.driver).edit_info(data)
        self.wait_success_tip()
        self.close_current_browser()
        self.switch_to_window(-1)
        return self

    @allure.step('选中年份')
    def select_year(self, year):
        self.locator_tree_node_click(node_value=year)
        return self
