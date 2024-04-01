# encoding=utf-8

from common.tools_packages import *
from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage


class CourseTag(EduSourcePage):

    @allure.step('查询标签')
    def search_tag(self, value: str = ''):
        self.locator_search_input(placeholder='名称', value=value, times=2, enter=True)
        return self

    def _edit_info(self, data: dict):
        if '关键字名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['关键字名称'])
        time.sleep(2)
        self.locator_button(button_title='保存')

    @allure.step('新增课表标签')
    def add_tag(self, data):
        self.locator_button(button_title='新增')
        self._edit_info(data)
        self.wait_success_tip()
        return self

    @allure.step('删除课表标签')
    def del_tag(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导出课表标签文件')
    def download_file(self):
        self.locator_button(button_title='导出')
        return wait_file_down_and_clean(file_name='关键字列表.xlsx')