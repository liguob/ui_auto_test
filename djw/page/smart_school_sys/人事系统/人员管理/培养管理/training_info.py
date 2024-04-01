# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/7/27    9:43
============================
"""
import time
from common.base_page import BasePage


class TrainingInfoPage(BasePage):
    """培训详情信息页面"""

    def edit_info(self, values: dict, name: str = ''):
        # 判断是否需要填写姓名
        if name:
            dialog_title = '请选择'
            self.locator_search_magnifier(ctrl_id='person')
            self.locator_search_input(dialog_title=dialog_title, value=name, placeholder='输入关键字进行过滤', enter=True)
            self.locator_tree_node_click(dialog_title=dialog_title, node_value=name)
            self.locator_dialog_btn(dialog_title=dialog_title, btn_name='确定')
        keys = values.keys()
        if "培训班名称" in keys:
            self.locator_text_input(ctrl_id='class_name', value=values["培训班名称"])
        if "主办单位" in keys:
            self.locator_text_input(ctrl_id='host_unit', value=values["主办单位"])
        if "年度" in keys:
            self.locator_text_input(ctrl_id='year', value=values["年度"], is_readonly=True)
        if "培训天数" in keys:
            self.locator_text_input(ctrl_id='training_day', value=values["培训天数"])
        if "培训开始日期" in keys:
            self.locator_date_range(ctrl_id='training_date', start_date=values["培训开始日期"], end_date=values["培训结束日期"])
        if "培训类别" in keys:
            self.locator_select_list_value(ctrl_id='training_type', value=values["培训类别"])
        if "培训地点" in keys:
            self.locator_text_input(ctrl_id='training_site', value=values["培训地点"])
        if "培训成果" in keys:
            self.locator_text_input(ctrl_id='training_outcome', value=values["培训成果"], is_file=True)
        if "培训内容" in keys:
            self.locator_text_input(ctrl_id='training_content', value=values["培训内容"], tag_type='textarea')
        if "备注" in keys:
            self.locator_text_input(ctrl_id='notes', value=values["备注"], tag_type='textarea')
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self
