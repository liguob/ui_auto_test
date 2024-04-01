# encoding=utf-8
"""
============================
Author:
Time:
============================
"""

from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class RuleCheckPage(PersonnelSysPage):
    """规章制度查看页面类"""

    @allure.step('搜索')
    def search_rule(self, title):
        self.locator_search_input(placeholder='请输入标题', times=2, enter=True, value=title)
        return self

    @allure.step('查看规则制度详情')
    def view_info(self, title):
        self.locator_view_button(button_title='查看', id_value=title)
        self.wait_open_new_browser_and_switch()
        title_loc = (By.CSS_SELECTOR, '[ctrl-id="title"] [title]')
        title_text = self.get_ele_text_visitable(title_loc)
        self.close_and_return_page()
        return title_text
