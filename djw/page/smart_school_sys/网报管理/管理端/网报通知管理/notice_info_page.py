# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/10/14 16:55
@Author :李国彬
============================
"""
import time

from selenium.webdriver.common.by import By

from common.base_page import BasePage


class NoticeInfoPage(BasePage):
    """网报通知管理编辑信息"""

    def edit_notice_info(self, values: dict):
        keys = values.keys()
        if '标题' in keys:
            self.locator_text_input(ctrl_id='title', value=values['标题'])
        if '正文' in keys:
            text_input = (By.XPATH, '//body[@contenteditable="true"]/p')
            edit_frame = (By.CSS_SELECTOR, 'iframe[id*="ueditor"]')
            self.switch_to_frame(loc=edit_frame)
            self.clear_and_input(text_input, value=values['正文'])
            self.switch_to_frame_back()
        if '附件' in keys:
            self.locator_text_input(ctrl_id='annex', value=values['附件'], is_file=True)
        if '通知单位' in keys:
            self.locator_button(button_title='选择')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=values['通知单位'], enter=True)
            self.locator_tree_node_click(node_value=values['通知单位'])
            self.locator_dialog_btn(btn_name='确定')
        time.sleep(2)



