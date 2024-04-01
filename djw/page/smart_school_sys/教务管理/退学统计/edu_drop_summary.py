from time import sleep

import allure
from selenium.webdriver.common.by import By
from common.file_path import wait_file_down_and_clean
from djw.page.smart_school_sys.班主任管理.退学统计.drop_count_page import DropCountPage


class EduDropSummary(DropCountPage):
    """教务管理-综合统计-退学统计"""

    @allure.step('班次列表导出')
    def export_classes(self, file_name: str = '数据导出.xlsx'):
        sleep(0.5)
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name="导出", dialog_title="导出设置", need_close=True)
        return wait_file_down_and_clean(file_name=file_name)

    @allure.step('退学学员列表导出')
    def export_stus(self, file_name: str = '学员退学表.xlsx'):
        export_btn = (By.CSS_SELECTOR, '.el-dialog [title="导出"].ds-button')
        self.excute_js_click_ele(export_btn)
        self.locator_dialog_btn(btn_name="导出", dialog_title="导出设置", need_close=True)
        return wait_file_down_and_clean(file_name=file_name)
