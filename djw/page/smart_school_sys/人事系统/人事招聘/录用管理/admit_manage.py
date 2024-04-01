# encoding=utf-8
"""
============================
Author:何凯
Time:2021/9/6 18:56
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AdmitManage(PersonnelSysPage):
    """录用管理页面类"""

    @allure.step('查询人员')
    def search_user(self, name):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name, times=2, enter=True)
        return self

    @allure.step('录用人员')
    def admit_user(self, name):
        self.locator_view_button(button_title='录用', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('不录用人员')
    def reject_user(self, name):
        self.locator_view_button(button_title='不录用', id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('查看人员')
    def view_user(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self.get_ele_text_visitable((By.CSS_SELECTOR, '[ctrl-id=name] [title]'))


