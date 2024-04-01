# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/13    16:03
============================
"""
import time

import allure

from time import sleep
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class SchoolAndBuildingManagePage(BasePage):
    """管理校区/楼宇页面"""
    root_node = (By.XPATH, '//*[@role="tree"]/div[1]/div[1]//span[text()]')  # 校区楼宇树的根节点

    @allure.step("选择校区/楼宇/楼层")
    def select_building_tree(self, name):
        self.search_building_tree(name)
        xpath = (By.XPATH, '//span[text()="{}"]'.format(name))
        self.excute_js_click(xpath)
        sleep(1)
        return self

    @allure.step("删除校区")
    def del_school(self, school_name):
        """点击根节点，查询校区后删除"""
        root_node = (By.XPATH, '//*[@role="tree"]/div[1]/div[1]//span[text()]')
        self.excute_js_click(root_node)
        self.search_building_view(school_name)
        self.locator_view_button(button_title="删除", id_value=school_name)
        self.locator_dialog_btn("确定")
        self.wait_tip()
        return self

    @allure.step("删除楼宇")
    def del_build(self, school_name, build_name):
        """选中校区后，删除对应的楼宇"""
        self.select_building_tree(school_name)
        time.sleep(1)
        self.locator_view_button(button_title="删除", id_value=build_name)
        self.locator_dialog_btn("确定")
        self.wait_tip()
        return self

    @allure.step("删除楼层")
    def del_floor(self, build_name, floor_name):
        """选中楼宇后，删除对应的楼层"""
        self.select_building_tree(build_name)
        self.locator_view_button(button_title="删除", id_value=floor_name)
        self.locator_dialog_btn("确定")
        self.wait_tip()
        return self

    @allure.step("返回场地库管理主页")
    def go_site_main_page(self):
        """关闭校区/楼宇管理页面回到，场地库管理主页面"""
        self.driver.close()
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.教学资源.场地库管理.site_manage_main_page import SiteManageMainPage
        return SiteManageMainPage(self.driver)

    @allure.step("填写楼宇信息")
    def _edit_building_info(self, values: dict):
        keys = values.keys()
        # 楼宇信息
        if "楼宇名称" in keys:
            self.locator_text_input(ctrl_id="name", value=values["楼宇名称"])
        if "楼宇简称" in keys:
            self.locator_text_input(ctrl_id="alias", value=values["楼宇简称"])
        if "排序码" in keys:
            self.locator_text_input(ctrl_id="ds_order", value=values["排序码"])
        if "备注" in keys:
            self.locator_text_input(ctrl_id="remark", value=values["备注"], tag_type='textarea')
        self.locator_button("保存")
        sleep(2)  # 等待界面自动刷新

    @allure.step("填写校区信息")
    def _edit_school_info(self, values: dict):
        keys = values.keys()
        if "校区名称" in keys:
            self.locator_text_input(ctrl_id="name", value=values["校区名称"])
        if "校区简称" in keys:
            self.locator_text_input(ctrl_id="alias", value=values["校区简称"])
        if "排序码" in keys:
            self.locator_text_input(ctrl_id="ds_order", value=values["排序码"])
        if "备注" in keys:
            self.locator_text_input(ctrl_id="remark", value=values["备注"], tag_type='textarea')
        self.locator_button("保存")
        sleep(2)  # 等待界面自动关闭

    @allure.step("填写楼层信息")
    def _edit_floor_info(self, values: dict):
        keys = values.keys()
        if "楼层名称" in keys:
            self.locator_text_input(ctrl_id="name", value=values["楼层名称"])
        if "楼层简称" in keys:
            self.locator_text_input(ctrl_id="alias", value=values["楼层简称"])
        if "排序码" in keys:
            self.locator_text_input(ctrl_id="ds_order", value=values["排序码"])
        if "备注" in keys:
            self.locator_text_input(ctrl_id="remark", value=values["备注"], tag_type='textarea')
        self.locator_button("保存")
        sleep(2)  # 等待界面自动关闭

    @allure.step("查询楼宇/校区/楼层列表")
    def search_building_view(self, value):
        """根据名称查询"""
        self.locator_search_input(placeholder='请输入检索关键字', value=value)
        self.locator_tag_search_button()
        sleep(2)  # 等待查询加载
        return self

    @allure.step("查询校区/楼宇/楼层树")
    def search_building_tree(self, name):
        self.locator_search_input(placeholder='请输入查询关键字', value=name, enter=True, times=1)
        return self

    @allure.step("新增校区")
    def add_school(self, values: dict):
        self.locator_button(button_title="新增校区")
        self.wait_open_new_browser_and_switch()
        self._edit_school_info(values)
        self.switch_to_window(-1)
        return self

    @allure.step("新增楼宇")
    def add_building(self, school_name, values: dict):
        """先点击选择校区，再在该校区下创建楼宇"""
        self.select_building_tree(school_name)
        self.locator_button(button_title="新增楼宇")
        self.wait_open_new_browser_and_switch()
        self._edit_building_info(values)
        self.switch_to_window(-1)
        return self

    @allure.step("新增楼层")
    def add_floor(self, build_name, values: dict):
        """先点击选择楼宇，再在该楼宇下创建楼层"""
        self.select_building_tree(build_name)
        self.locator_button(button_title="新增楼层")
        self.wait_open_new_browser_and_switch()
        self._edit_floor_info(values)
        self.switch_to_window(-1)
        return self

    @allure.step("新增校区校验")
    def add_school_check(self, values: dict):
        """先点击选择校区，再在该校区下创建楼宇"""
        self.locator_button(button_title="新增校区")
        self.wait_open_new_browser_and_switch()
        self._edit_school_info(values)
        return self.get_tip_info()

    @allure.step("修改校区")
    def edit_school(self, school_name, values: dict):
        self.excute_js_click(self.root_node)
        self.locator_view_button(button_title="编辑", id_value=school_name)
        self.wait_open_new_browser_and_switch()
        sleep(1)
        self._edit_school_info(values)
        self.switch_to_window(-1)
        return self

    @allure.step("修改楼宇")
    def edit_building(self, building_name, values: dict):
        self.select_building_tree(building_name)
        self.locator_button(button_title='修改校区信息')
        self.wait_open_new_browser_and_switch()
        sleep(3)
        self._edit_building_info(values)
        self.switch_to_window(-1)
        return self

    @allure.step("修改楼层")
    def edit_floor(self, floor_name, values: dict):
        self.select_building_tree(floor_name)
        self.locator_button(button_title='修改校区信息')
        self.wait_open_new_browser_and_switch()
        sleep(3)
        self._edit_floor_info(values)
        self.switch_to_window(-1)
        return self

    @allure.step("获取提示信息")
    def get_tip_info(self):
        """校验信息时，获取提示信息文本"""
        # 弹出的提示信息元素
        self.switch_to_frame_back()
        tip_info = (By.CSS_SELECTOR, '.ds-error-text')
        return self.find_elem(tip_info).text

    @allure.step("返回场地库管理主页")
    def back_site_manage_page(self):
        self.close_current_browser()
        self.switch_to_window(-1)
        self.refresh()
        time.sleep(3)  # 等待刷新加载
        from djw.page.smart_school_sys.教学资源.场地库管理.site_manage_main_page import SiteManageMainPage
        return SiteManageMainPage(self.driver)

