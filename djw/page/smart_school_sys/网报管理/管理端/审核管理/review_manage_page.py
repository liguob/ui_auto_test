# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 16:48
@Author :李国彬
============================
"""
import allure

from djw.page.smart_school_sys.主页.home_page import HomePage


class ReviewManagePage(HomePage):
    """审核管理主页"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入报名审核页面')
    def go_review_detail_page(self, name):
        self.locator_view_button(button_title='报名审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.网报管理.管理端.审核管理.review_detail_page import ReviewDetailPage
        return ReviewDetailPage(self.driver)
