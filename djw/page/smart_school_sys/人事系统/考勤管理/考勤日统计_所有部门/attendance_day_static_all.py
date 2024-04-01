from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.考勤管理.考勤日统计_当前部门.attendance_day_static_cur import \
    AttendanceDayStaticCur


class AttendanceDayStaticAll(AttendanceDayStaticCur):

    @allure.step('选中部门')
    def select_dept(self, dept):
        self.locator_search_input(placeholder='请输入查询关键字', value=dept, enter=True)
        self.locator_tree_node_click(node_value=dept)
        return self
