# encoding=utf-8
from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class ResumeCheck(PersonnelSysPage):
    """简历审核页面"""

    @allure.step('查询简历')
    def search_apply(self, value):
        self.locator_tag_search_input(placeholder='公告/岗位/姓名', value=value, enter=True, times=2)
        return self

    @allure.step('审核不同意')
    def disagree_apply(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(3)
        self.locator_button(button_title='不同意')
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('审核同意')
    def agree_apply(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.locator_button(button_title='同意')
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('查看审核详情')
    def view_apply(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self.get_ele_text_visitable((By.CSS_SELECTOR, '[ctrl-id="phone"] [title]'))
