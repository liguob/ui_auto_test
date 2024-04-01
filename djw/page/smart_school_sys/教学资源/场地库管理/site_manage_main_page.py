# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/13    15:32
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage


class SiteManageMainPage(EduSourcePage):
    """场地管理主页"""

    @allure.step("选择校区/楼宇")
    def select_building_tree(self, name):
        self.locator_search_input(placeholder='请输入查询关键字', value=name, enter=True, times=1)
        self.locator_tree_node_click(node_value=name, times=2)
        return self

    @allure.step("进入管理校区/楼宇")
    def goto_school_building_page(self):
        self.locator_more_tip_button(button_title='管理校区/楼宇')
        # 切换到新窗口
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教学资源.场地库管理.school_build_manage_page import SchoolAndBuildingManagePage
        time.sleep(2)
        return SchoolAndBuildingManagePage(self.driver)

    @allure.step("删除场地")
    def del_site(self, parent_name, site_name):
        """选择场地上级校区或者楼宇，再选择场地进行删除"""
        self.select_building_tree(parent_name)
        self.locator_view_button(button_title="删除", id_value=site_name)
        self.locator_dialog_btn("确定")
        self.wait_success_tip()
        return self

    @allure.step("新增场地")
    def add_site(self, name, values: dict):
        """选择对应的校区/楼宇/楼层名称，新增场地"""
        self.select_building_tree(name)
        self.locator_button(button_title="新增场地")
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教学资源.场地库管理.site_info_page import SiteInfoPage
        SiteInfoPage(self.driver).edit_site_info(values)
        self.wait_success_tip()
        self.close_and_return_page()
        return self

    @allure.step("编辑场地")
    def edit_site(self, parent_name, site_name, values: dict):
        """选择对应的校区或场地名称下，编辑场地"""
        self.select_building_tree(parent_name)
        self.locator_view_button(button_title="编辑", id_value=site_name)
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value(ctrl_id='name')
        from djw.page.smart_school_sys.教学资源.场地库管理.site_info_page import SiteInfoPage
        SiteInfoPage(self.driver).edit_site_info(values)
        self.wait_success_tip()
        self.close_and_return_page()
        return self

    @allure.step("新增场地校验")
    def add_site_check(self, name, values: dict):
        """选择对应的校区/楼宇/楼层名称，新增场地"""
        self.select_building_tree(name)
        self.locator_button(button_title="新增场地")
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教学资源.场地库管理.site_info_page import SiteInfoPage
        return SiteInfoPage(self.driver).edit_site_info_check(values)

    @allure.step('查询场地')
    def search_site(self, value):
        self.locator_tag_search_input(placeholder='名称', value=value)
        self.locator_tag_search_button()
        return self
