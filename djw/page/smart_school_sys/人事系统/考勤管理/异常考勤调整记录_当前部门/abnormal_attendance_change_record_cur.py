from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AbnormalAttendanceChangeRecordCur(PersonnelSysPage):

    @allure.step('查询异常考勤修改人员')
    def search_user(self, name):
        self.locator_search_input(placeholder='姓名', value=name, enter=True)
        return self

    @allure.step('导出异常考勤修改信息文件')
    def download_file(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='数据导出.xlsx')
