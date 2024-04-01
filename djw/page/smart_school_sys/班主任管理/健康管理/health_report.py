from datetime import datetime
from common.tools_packages import *
from djw.page.smart_school_sys.班主任管理.master_manage_page import MasterManagePage


class HealthReportPage(MasterManagePage):
    """日常管理-健康报告"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name, times=2, enter=True)
        return self

    @allure.step('进入指定班次健康状况详情')
    def into_health_statistics(self, class_name):
        self.locator_view_button(button_title='健康状况', id_value=class_name)
        self.wait_open_new_browser_and_switch()
        time.sleep(3)
        return self

    @allure.step('点击数量查看统计详情信息')
    def click_num_view_info(self):
        self.excute_js_click((By.CSS_SELECTOR, '[class*="healthsummarydb_zcnum__value"]>a'))
        time.sleep(2)
        return self.locator_view_num(dialog_title='对话框')
