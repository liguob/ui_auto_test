from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AttendanceMonthStaticCur(PersonnelSysPage):

    @allure.step('查询考勤月份')
    def search_month(self, month):
        self.locator_search_input(placeholder='月份(yyyy-mm)/部门', value=month, enter=True)
        return self

    @allure.step('查看考勤详情')
    def view_detail(self, dept):
        self.locator_view_button(button_title='考勤详情', id_value=dept)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('查询考勤人员')
    def search_user(self, name):
        self.locator_search_input(placeholder='姓名', value=name, enter=True)
        return self

    @allure.step('导出人员')
    def download_file(self, file_name):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name=file_name)