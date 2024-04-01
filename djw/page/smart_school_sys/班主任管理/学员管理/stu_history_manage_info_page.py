# coding: utf-8
"""
============================
# Time      ：2022/3/21 15:35
# Author    ：李国彬
============================
"""
from common.base_page import BasePage
from common.tools_packages import *


class StuHistoryManageInfo(BasePage):
    """历史班次学员查看页面"""

    @allure.step('导出学员')
    def export_stu(self, class_name):
        self.locator_tag_button('导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(f'{class_name}_学员信息.xlsx')

    @allure.step('导出学员照片')
    def export_stu_pic(self, class_name):
        self.locator_tag_button('照片导出')
        return wait_file_down_and_clean(f'{class_name}-学员照片.zip')
