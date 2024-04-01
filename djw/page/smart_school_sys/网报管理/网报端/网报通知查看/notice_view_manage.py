# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 17:47
@Author :李国彬
============================
"""
import allure

from common.base_page import BasePage


class NoticeViewManagePage(BasePage):
    """网报通知查看页面"""

    @allure.step('查询网报通知')
    def search_notice(self, name):
        self.locator_search_input(placeholder='标题', value=name)
        self.locator_tag_search_button()
        return self
