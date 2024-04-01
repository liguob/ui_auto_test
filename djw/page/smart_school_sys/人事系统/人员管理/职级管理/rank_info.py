# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/27    10:34
============================
"""
import time

from common.base_page import BasePage


class RankManegeInfo(BasePage):
    """职级管理详细信息页面"""

    def edit_info(self, values: dict, name: str = ''):
        if name:
            dialog_title = '请选择'
            self.locator_search_magnifier(ctrl_id='person')
            self.locator_search_input(dialog_title=dialog_title, value=name, placeholder='输入关键字进行过滤', enter=True)
            time.sleep(2)  # 等待查询结果
            self.locator_tree_node_click(dialog_title=dialog_title, node_value=name)
            self.locator_dialog_btn(dialog_title=dialog_title, btn_name='确定')
        keys = values.keys()
        if "职级名称" in keys:
            self.locator_select_list_value(ctrl_id='rank', value=values["职级名称"])
        if "自定义职级" in keys:
            self.locator_text_input(ctrl_id='custom_rank', value=values["自定义职级"])
        if "评定日期" in keys:
            self.locator_date(ctrl_id='evaluate_date', value=values["评定日期"])
        if "任职部门" in keys:
            self.locator_text_input(ctrl_id='take_dept', value=values["任职部门"])
        if "附件" in keys:
            self.locator_text_input(ctrl_id='file', value=values["附件"], is_file=True)
        if "备注" in keys:
            self.locator_text_input(ctrl_id='notes', value=values["备注"], tag_type='textarea')
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self
