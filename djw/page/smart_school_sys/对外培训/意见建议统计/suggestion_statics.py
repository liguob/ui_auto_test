# coding: utf-8
"""
============================
# Time      ：2022/5/20 10:26
# Author    ：李国彬
============================
"""
from djw.page.smart_school_sys.主页.home_page import HomePage
from common.tools_packages import *


class SuggestionStatics(HomePage):
    """意见建议统计页面"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name, enter=True)
        return self

    def view_suggestion(self, class_name, view_type, suggestion_des):
        with allure.step(f'查看班次学员的{view_type}信息'):
            self.locator_view_value_click(id_value=class_name, header=view_type)
            time.sleep(2)
            self.locator_view_button(dialog_title=' ', button_title='查看', id_value=suggestion_des)
        time.sleep(3)
        suggestion_text = (By.CSS_SELECTOR, '.comments_content')
        info = self.get_text_implicitly(suggestion_text).strip()
        # 关闭两个弹窗窗口
        close_dialog = (By.CSS_SELECTOR, '.el-dialog__close')
        close_bt = self.find_elms(close_dialog)
        self.excute_js_click_ele(close_bt[1])
        self.excute_js_click_ele(close_bt[0])
        time.sleep(2)
        return info
