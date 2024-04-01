# encoding=utf-8
"""
============================
Author:何超
Time:2021/08/22
============================
"""
import time

import allure
from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class LeaveAndVacationPage(PersonnelSysPage):
    """人事系统请休假申请页面类"""
    btn_yes = (By.XPATH, '//span[contains(text(),"确定")]/..')  # 确定按钮
    tip_success = (By.XPATH, '//*[@*="el-message el-message--success"]')  # 成功的提示

    @allure.step("获取请休假列表信息")
    def get_leave_and_vacation_info(self):
        list_item_loc = (By.XPATH, '//*[contains(@class,"is-scrolling")]//td[{}]')
        list_item = [(list_item_loc[0], list_item_loc[1].format(i)) for i in range(2, 7)]
        title = ('time', 'type', 'commit_time', 'reason', 'status')
        try:
            value = self.publish_get_info(*list_item, t=title)
            return value
        except Exception:
            return []

    @allure.step("新增请休假申请")
    def into_leave_and_vacation(self):
        from djw.page.smart_school_sys.人事系统.请休假管理.请休假申请.leaveandvacationapply import LeaveAndVacationApply
        btn = (By.XPATH, '//*[text()=" 新建请假单 "]/parent::a')
        self.excute_js_click_ele(btn)
        self.switch_to_handle()
        return LeaveAndVacationApply(self.driver)

    @allure.step("查看请休假申请")
    def into_check_leave_and_vacation(self, index=1):
        from djw.page.smart_school_sys.人事系统.请休假管理.请休假申请.leaveandvacationapply import LeaveAndVacationApply
        btn = (By.XPATH, '(//*[@*="el-table__fixed-right"]//span[text()=" 查看 "]/parent::a)[{}]'.format(index))
        self.element_click(btn)
        self.switch_to_handle()
        return LeaveAndVacationApply(self.driver)

    @allure.step("编辑请休假申请")
    def into_check_leave_and_vacation_edit(self, index=1):
        from djw.page.smart_school_sys.人事系统.请休假管理.请休假申请.leaveandvacationapply import LeaveAndVacationApply
        self.locator_view_button(button_title="编辑", id_value=str(index))
        self.switch_to_handle()
        return LeaveAndVacationApply(self.driver)

    def delete_leave_and_vacation(self, index=1):
        self.locator_view_button(button_title="删除", id_value=str(index))
        self.element_click(self.btn_yes)
        self.explicit_wait_ele_lost(self.WEB_TIP)
        return self

    @allure.step('搜索请休假申请')
    def search_leave_apply(self, reason):
        """reason:请休假事由"""
        self.locator_tag_search_input(placeholder='请输入请休假事由', value=reason)
        search_btn = (By.CSS_SELECTOR, '.search-button')
        self.poll_click(search_btn)
        time.sleep(0.5)
        self.wait_presence_list_data()
        return self
