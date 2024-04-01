from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage


class SchoolRollQueryClass(HomePage):

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name, enter=True)
        return self

    @allure.step('点击查看班次')
    def view(self, class_name):
        self.locator_view_button(button_title='查看', id_value=class_name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('查询学员')
    def search_stu(self, name):
        self.locator_search_input(placeholder='请输入姓名', enter=True, value=name, times=2)
        return self

    @allure.step('查看学员详情')
    def view_stu(self, stu_name):
        self.locator_view_button(button_title='查看', id_value=stu_name)
        self.wait_open_new_browser_and_switch()
        name = (By.CSS_SELECTOR, f'[title="{stu_name}"]')
        return self.get_ele_text_visitable(name)
