# coding: utf-8
"""
============================
# Time      ：2022/5/20 10:26
# Author    ：李国彬
============================
"""

from common.tools_packages import *
from djw.page.smart_school_sys.对外培训.意见建议统计.suggestion_statics import SuggestionStatics


class SuggestionReply(SuggestionStatics):
    """意见建议回复"""

    def reply_suggestion(self, class_name, suggestion_des, reply_str):
        reply_input = (By.CSS_SELECTOR, 'textarea[placeholder="请输入您的回复"]')
        with allure.step(f'回复班次学员的意见建议'):
            self.locator_view_value_click(id_value=class_name, header='未回复')
            self.locator_view_button(dialog_title=' ', button_title='回复', id_value=suggestion_des)
            self.find_elem_visibility(reply_input).send_keys(reply_str)
            time.sleep(1)  # 等待回复按钮可点击
            self.locator_dialog_btn(dialog_title='查看意见与建议', btn_name='回复')
            time.sleep(1)
        # 关闭弹窗
        close_dialog = (By.CSS_SELECTOR, '.el-dialog__close')
        self.excute_js_click(close_dialog)
        time.sleep(2)
        return self
