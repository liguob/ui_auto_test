import allure
from time import sleep

from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage


class SiteOccupation(HomePage):
    search_btn = (By.CSS_SELECTOR, '[class="ds-button small"]>span')

    @allure.step('查询教室占用')
    def search(self, site_name):
        btn_select = (By.CSS_SELECTOR, '[title="场地"]+div i')
        self.excute_js_click(btn_select)
        value_select = (By.XPATH, f'//*[text()="{site_name}"]')
        self.excute_js_click(value_select)
        self.element_click(self.search_btn)
        return self

    @allure.step('导出')
    def download_type_info(self):
        self.locator_dialog_btn('导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean('场地占用统计.xlsx')





