from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AbnormalAttendanceCur(PersonnelSysPage):

    @allure.step('查询异常考勤人员')
    def search_user(self, name):
        self.locator_search_input(placeholder='姓名', value=name, enter=True)
        return self

    @allure.step('修改异常考勤状态')
    def edit_attendance(self, name):
        self.locator_view_button(button_title='修改', id_value=name)
        self.locator_dialog_btn(btn_name='正常', dialog_title='考勤结果将修改为')
        self.locator_dialog_btn(btn_name='确认')
        self.wait_success_tip()
        return self

    @allure.step('导出异常考勤信息文件')
    def download_file(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='数据导出.xlsx')
