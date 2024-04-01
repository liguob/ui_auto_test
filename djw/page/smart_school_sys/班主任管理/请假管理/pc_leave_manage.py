# encoding=utf-8
from common.tools_packages import *
from djw.page.smart_school_sys.班主任管理.master_manage_page import MasterManagePage


class PcLeaveManage(MasterManagePage):
    """pc端请假管理页面"""

    @allure.step("查询班次")
    def search_class(self, class_name):
        """搜索班次"""
        self.locator_tag_search_input(placeholder='班次名称', value=class_name, enter=True)
        return self

    @allure.step("进入当前班次的请假详情")
    def into_leave_detail(self, value):
        """进入请假详情页面"""
        self.locator_view_button(button_title='请假详情', id_value=value)
        from djw.page.smart_school_sys.班主任管理.请假管理.leave_detail_page import LeaveDetailPage
        self.wait_open_new_browser_and_switch()
        return LeaveDetailPage(self.driver)
