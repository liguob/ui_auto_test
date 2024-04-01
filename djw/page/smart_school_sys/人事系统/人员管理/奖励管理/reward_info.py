# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/27    10:06
============================
"""
import time

from common.base_page import BasePage


class RewardManageInfo(BasePage):
    """奖励管理详情信息页面"""

    def edit_info(self, values: dict, name: str = ''):
        # 判断是否需要填写姓名
        if name:
            dialog_title = '请选择'
            self.locator_search_magnifier(ctrl_id='person')
            self.locator_search_input(dialog_title=dialog_title, value=name, placeholder='输入关键字进行过滤', enter=True)
            time.sleep(2)  # 等待查询结果
            self.locator_tree_node_click(dialog_title=dialog_title, node_value=name)
            self.locator_dialog_btn(dialog_title=dialog_title, btn_name='确定')
        keys = values.keys()
        if "奖励名称" in keys:
            self.locator_text_input(ctrl_id='name', value=values["奖励名称"])
        if "年度" in keys:
            self.locator_text_input(ctrl_id='year', value=values['年度'], is_readonly=True)
        if "奖励单位名称" in keys:
            self.locator_text_input(ctrl_id='award_unit', value=values["奖励单位名称"])
        if "奖励类别" in keys:
            self.locator_select_list_value(ctrl_id='type', value=values["奖励类别"])
        if "授奖日期" in keys:
            self.locator_date(ctrl_id='award_date', value=values["授奖日期"])
        if "奖励文号" in keys:
            self.locator_text_input(ctrl_id='award_number', value=values["奖励文号"])
        if "奖励单位级别" in keys:
            self.locator_select_list_value(ctrl_id='award_unit_level', value=values["奖励单位级别"])
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self
