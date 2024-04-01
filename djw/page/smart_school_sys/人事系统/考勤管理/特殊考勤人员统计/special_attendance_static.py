from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class SpecialAttendanceStatic(PersonnelSysPage):

    @allure.step('查询人员')
    def search_user(self, name):
        self.locator_tag_search_input(placeholder='姓名', value=name, enter=True)
        return self

    @allure.step('特殊考勤统计导出')
    def download_file(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('数据导出.xlsx')

    @allure.step('点击考勤详情')
    def view_detail(self, name):
        self.locator_view_button(button_title='考勤详情', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('特殊考勤人员导出')
    def download_detail_file(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('数据导出.xlsx')
