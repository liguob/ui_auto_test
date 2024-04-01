# -*- coding: utf-8 -*-
"""
===============================
@Time     ：2021/9/3 11:25
@Author   ：李国彬
===============================
"""
import time

from common.base_page import BasePage


class TemporaryTrainingInfoPage(BasePage):
    """挂职培训详情页面"""

    def edit_info(self, values: dict):
        keys = values.keys()
        if '标题' in keys:
            self.locator_text_input(ctrl_id='title', value=values['标题'])
        if '类型' in keys:
            self.locator_select_list_value(ctrl_id='type', value=values['类型'])
        if '参加人员' in keys:
            dialog_title = '请选择'
            self.locator_search_magnifier(ctrl_id='persons')
            self.locator_search_input(dialog_title=dialog_title, placeholder='输入关键字进行过滤', value=values['参加人员'], enter=True)
            time.sleep(2)
            self.locator_tree_node_click(dialog_title=dialog_title, node_value=values['参加人员'])
            self.locator_dialog_btn(dialog_title=dialog_title, btn_name='确定')
        if '年度' in keys:
            self.locator_text_input(ctrl_id='year', value=values['年度'], is_readonly=True)
        if '有无证书' in keys:
            self.locator_select_list_value(ctrl_id='certificate', value=values['有无证书'])
        if '挂职部门' in keys:
            self.locator_text_input(ctrl_id='dept', value=values['挂职部门'])
        if '培训单位' in keys:
            self.locator_text_input(ctrl_id='unit', value=values['培训单位'])
        if '培训班次' in keys:
            self.locator_text_input(ctrl_id='classname', value=values['培训班次'])
        if '附件' in keys:
            self.locator_text_input(ctrl_id='annex', value=values['附件'], is_file=True)
        if '备注' in keys:
            self.locator_text_input(ctrl_id='remark', value=values['备注'], tag_type='textarea')
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self
