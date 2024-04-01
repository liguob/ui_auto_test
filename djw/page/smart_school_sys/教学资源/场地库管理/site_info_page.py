# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/13    16:01
============================
"""
import time

import allure
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class SiteInfoPage(BasePage):

    @allure.step("填写场地信息")
    def edit_site_info(self, values: dict):
        """填写场地信息"""
        keys = values.keys()
        if "名称" in keys:
            self.locator_text_input(ctrl_id="name", value=values["名称"])
        if "排序码" in keys:
            self.locator_text_input(ctrl_id="ds_order", value=values["排序码"])
        if "简称" in keys:
            self.locator_text_input(ctrl_id="alias", value=values["简称"])
        if "教室类型" in keys:
            self.locator_select_list_value(ctrl_id="type", value=values["教室类型"])
            text_label = (By.CSS_SELECTOR, '[ctrl-id=type] label')
            self.move_to_click(text_label)
        if "容纳人数" in keys:
            self.locator_text_input(ctrl_id="num", value=values["容纳人数"])
        if "多媒体场地" in keys:
            self.locator_select_radio(ctrl_id='is_multi_media', value=values["多媒体场地"])
        if "多媒体资源" in keys:
            self.locator_select_radio(ctrl_id="facility", value=values["多媒体资源"])
        if "状态" in keys:
            self.locator_select_radio(ctrl_id='status', value=values["状态"])
        if "教室排数" in keys:
            self.locator_text_input(ctrl_id="classroom_row", value=values["教室排数"])
        if "教室列数" in keys:
            self.locator_text_input(ctrl_id="classroom_column", value=values["教室列数"])
        self.locator_button("保存")

    @allure.step("填写场地信息失败并返回提示信息")
    def edit_site_info_check(self, values: dict):
        self.edit_site_info(values)
        tip_info = (By.CSS_SELECTOR, '.ds-error-text')  # 提示信息
        return self.get_ele_text_visitable(tip_info)
