from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class AttendanceType(PersonnelSysPage):
    """考勤种类"""

    @allure.step('考勤种类名称')
    def search_type(self, name):
        self.locator_search_input(placeholder='考勤种类名称', value=name, enter=True)
        return self

    @allure.step('新增考勤种类')
    def add_type(self, data: dict):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤种类.attendance_type_detail import AttendanceTypeDetail
        AttendanceTypeDetail(self.driver).edit_info(data)
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('编辑考勤种类')
    def edit_type(self, name, data: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value(ctrl_id='name')
        from djw.page.smart_school_sys.人事系统.考勤管理.考勤种类.attendance_type_detail import AttendanceTypeDetail
        AttendanceTypeDetail(self.driver).edit_info(data)
        self.wait_browser_close_switch_latest()

    @allure.step('删除考勤种类')
    def del_type(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self
