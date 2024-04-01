from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AttendanceApplyCheck(PersonnelSysPage):

    @allure.step('查询申请')
    def search_apply(self, name):
        self.locator_tag_search_input(placeholder='姓名', value=name, enter=True)
        return self

    @allure.step('下载申请文件')
    def download_file(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='确定')
        return wait_file_down_and_clean(file_name='数据导出.xlsx')

    @allure.step('申请审核通过')
    def apply_pass(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.locator_button(button_title='审核通过')
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('申请审核不通过')
    def apply_no_pass(self, name):
        self.locator_view_button(button_title='审核', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        self.locator_button(button_title='审核不通过')
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self
