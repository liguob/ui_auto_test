# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage


class TeaTeachSummary(HomePage):

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称、姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('教师授课汇总导出')
    def download_total_info(self):
        self.locator_dialog_btn('导出')
        self.locator_dialog_btn('确定')
        return wait_file_down_and_clean('数据导出.xlsx')

    def into_user_info(self, class_name, title):
        """进入授课详情页面"""
        with allure.step(f"进入{title}页面信息"):
            self.locator_view_value_click(id_value=class_name, header=title)
        return self

    @allure.step('查询课程')
    def search_course(self, name):
        self.locator_tag_search_input(placeholder='请输入课程名称', value=name, enter=True)
        # self.locator_tag_search_button(dialog_title='授课详情')
        return self

    @allure.step('授课详情导出')
    def download_total_course(self):
        self.locator_dialog_btn('导出', dialog_title='授课详情')
        return wait_file_down_and_clean('授课列表.xlsx')




