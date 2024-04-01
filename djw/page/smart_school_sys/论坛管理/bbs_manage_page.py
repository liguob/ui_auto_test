# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2022/1/20 12:30
# Author     ：李国彬
============================
"""
import allure

from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage


class BBSManagePage(HomePage):

    @allure.step('进入评论模块列表')
    def go_comment_model_manage(self):
        self.locator_left_menu_click(button_title='评论模块列表')
        from djw.page.smart_school_sys.论坛管理.评论模块列表.comment_model_manage import CommentModelManage
        return CommentModelManage(driver=self.driver)

    @allure.step('进入板块信息')
    def go_model_info_manage(self):
        self.locator_left_menu_click(button_title='板块信息')
        from djw.page.smart_school_sys.论坛管理.板块信息.bbs_model_info_page import BbsModelInfoPage
        frame_loc = (By.CSS_SELECTOR, 'iframe[src]')
        self.switch_to_frame(loc=frame_loc)
        return BbsModelInfoPage(driver=self.driver)
