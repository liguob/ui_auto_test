# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/27    10:19
============================
"""
import time

from common.base_page import BasePage


class PunishInfoPage(BasePage):
    """惩罚管理详情信息页面"""

    def edit_info(self, values: dict, name: str = ''):
        if name:
            dialog_title = '请选择'
            self.locator_search_magnifier(ctrl_id='person')
            self.locator_search_input(dialog_title=dialog_title, value=name, placeholder='输入关键字进行过滤', enter=True)
            time.sleep(2)  # 等待查询结果
            self.locator_tree_node_click(dialog_title=dialog_title, node_value=name)
            self.locator_dialog_btn(dialog_title=dialog_title, btn_name='确定')
        keys = values.keys()
        if "惩处名称" in keys:
            self.locator_text_input(ctrl_id='name', value=values["惩处名称"])
        if "年度" in keys:
            self.locator_text_input(ctrl_id='year', value=values['年度'], is_readonly=True)
        if "惩处类别" in keys:
            self.locator_select_list_value(ctrl_id='type', value=values["惩处类别"])
        if "惩处日期" in keys:
            self.locator_date(ctrl_id='penalty_date', value=values["惩处日期"])
        if "惩处文号" in keys:
            self.locator_text_input(ctrl_id='penalty_number', value=values["惩处文号"])
        if "惩处单位名称" in keys:
            self.locator_text_input(ctrl_id='penalty_unit', value=values["惩处单位名称"])
        if "惩处单位级别" in keys:
            self.locator_select_list_value(ctrl_id='penalty_unit_level', value=values["惩处单位级别"])
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self
