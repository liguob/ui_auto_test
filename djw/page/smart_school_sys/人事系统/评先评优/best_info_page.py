# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/9 11:12
@Author :李国彬
============================
"""
import time
from common.base_page import BasePage


class BestInfoPage(BasePage):

    def edit_info(self, values: dict):
        keys = values.keys()
        if '标题' in keys:
            self.locator_text_input(ctrl_id='title', value=values['标题'])
        if '年份' in keys:
            self.locator_text_input(ctrl_id='year', value=values['年份'], is_readonly=True)
        if '评优人员' in keys:
            self.locator_search_magnifier(ctrl_id='persons')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=values['评优人员'], enter=True)
            time.sleep(1)
            self.locator_tree_node_click(node_value=values['评优人员'])
            self.locator_dialog_btn(btn_name='确定')
        if '附件' in keys:
            self.locator_text_input(ctrl_id='annex', value=values['附件'], is_file=True)
        time.sleep(1)
        self.locator_button(button_title='保存')
