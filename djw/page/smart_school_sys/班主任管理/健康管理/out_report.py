from common.tools_packages import *
from djw.page.smart_school_sys.班主任管理.master_manage_page import MasterManagePage


class OutReportPage(MasterManagePage):
    """健康管理-外出报备"""

    @allure.step('查看班次')
    def search_class(self, class_name):
        self.locator_tag_search_input(placeholder='班次名称', value=class_name)
        self.locator_tag_search_button(times=2)
        return self

    @allure.step('进入班次报备统计')
    def into_out_report_statistics(self, name):
        self.locator_view_button(button_title='报备统计', id_value=name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('查询外出报备人员')
    def search_user(self, name):
        self.locator_search_input(placeholder='姓名', value=name, times=2, enter=True)
        return self

    @allure.step('导出外出报备人员文件')
    def download_file(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='外出报备.xlsx')

    @allure.step('查看单条外出报备详情')
    def view_info(self, reason):
        self.locator_view_button(button_title='查看详情', id_value=reason)
        return self.get_ele_text_visitable((By.CSS_SELECTOR, '[ctrl-id="reason"] [title]'))