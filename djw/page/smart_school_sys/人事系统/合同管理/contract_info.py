# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/9/30 10:30
@Author :李国彬
============================
"""
import time

from common.base_page import BasePage


class ContractInfoPage(BasePage):
    """合同信息编辑界面"""

    def edit_info(self, values: dict):
        keys = values.keys()
        if '姓名' in keys:
            self.locator_search_magnifier(ctrl_id='person')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=values['姓名'], enter=True)
            self.locator_tree_node_click(node_value=values['姓名'])
            self.locator_dialog_btn(btn_name='确定')
        if '聘用部门' in keys:
            self.locator_text_input(ctrl_id='employ_post', value=values['聘用部门'])
        if '合同编号' in keys:
            self.locator_text_input(ctrl_id='serial', value=values['合同编号'])
        if '合同有效开始时间' in keys:
            self.locator_date_range(ctrl_id='signed', start_date=values['合同有效开始时间'], end_date=values['合同有效结束时间'])
        if '附件' in keys:
            self.locator_text_input(ctrl_id='file', is_file=True, value=values['附件'])
        time.sleep(2)  # 等待数据加载
        self.locator_button('保存')
