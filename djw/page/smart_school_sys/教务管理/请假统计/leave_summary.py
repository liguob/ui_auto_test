from common.tools_packages import *
from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class LeaveSummary(EduManagePage):
    """教务管理-请假统计页面类"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name, enter=True)
        return self

    @allure.step('点击请假次数进入班次请假详情信息')
    def into_class_leave_detail(self, name):
        click_value = (By.XPATH, f'//*[text()="{name}"]/ancestor::tbody//div[contains(@class, "leave_num")]')
        self.element_click(click_value)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('点击详情进入学员列表')
    def into_stu_leave_detail(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        return self

    @allure.step('导出请假明细文件')
    def download_file(self):
        self.locator_button('导出')
        self.locator_dialog_btn(btn_name="导出", dialog_title="导出设置", need_close=True)
        return wait_file_down_and_clean(file_name='请假明细.xlsx')

    @allure.step('导出学员请假列表文件')
    def download_stu_file(self):
        self.locator_button('导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title="导出设置", need_close=True)
        return wait_file_down_and_clean(file_name='学员请假列表.xlsx')

    @allure.step('查询学员')
    def search_stu(self, name):
        self.locator_search_input(placeholder='姓名、事由', value=name, enter=True)
        return self
