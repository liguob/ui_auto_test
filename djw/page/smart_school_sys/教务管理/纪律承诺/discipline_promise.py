from djw.page.smart_school_sys.主页.home_page import HomePage
from common.tools_packages import *


class DisciplinePromise(HomePage):
    """纪律承诺"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='班次名称', value=name, times=2, enter=True)
        return self

    @allure.step('导出记录承诺班次信息文件')
    def download_class_file(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='确定')
        return wait_file_down_and_clean(file_name='记录承诺.xlsx')

    @allure.step('导出记录承诺学员信息文件')
    def download_stu_file(self, dialog):
        self.locator_button(button_title='导出', dialog_title=dialog)
        self.locator_dialog_btn(btn_name='确定')
        return wait_file_down_and_clean(file_name='记录承诺.xlsx')

    @allure.step('查询学员')
    def search_stu(self, name):
        self.locator_search_input(placeholder='姓名/手机号码', value=name, enter=True, times=2)
        return self

    def into_stu_detail(self, header, name):
        with allure.step(f'点击进入{header}详情'):
            self.locator_view_value_click(header=header, id_value=name)
        return self
