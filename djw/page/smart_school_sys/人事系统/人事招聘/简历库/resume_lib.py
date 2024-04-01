# encoding=utf-8
"""
============================
Author:何凯
Time:2021/9/6 18:57
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class ResumeLib(PersonnelSysPage):
    """简历库页面"""

    @allure.step('查询简历')
    def search_resume(self, name):
        self.locator_search_input(placeholder='请输入姓名', value=name, enter=True, times=2)
        return self

    @allure.step('查看简历')
    def view_resume(self, name):
        self.locator_view_button(button_title='查看简历', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self.get_ele_text_visitable((By.CSS_SELECTOR, '[ctrl-id=name] [title]'))

