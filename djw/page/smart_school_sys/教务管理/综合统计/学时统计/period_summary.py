import typing
import json
import random
from common.tools_packages import *
from common.decorators import change_reset_implicit


class PeriodSummary(BasePage):

    @property
    def mapping(self):
        return {'未开始班次': '#pane-NotStarted', '当前班次': '#pane-underway', '历史班次': '#finished'}

    @allure.step('检索班次')
    def search_class(self, class_name: str, tab_name: typing.Literal['未开始班次', '当前班次', '历史班次'] = '当前班次'):
        self.locator_switch_tag(tag_name=tab_name)
        self.locator_tag_search_input(placeholder='请输入班次名称', value=class_name)
        self.locator_tag_search_button()
        return self

    @property
    @allure.step('获取列表某班总课时')
    def list_total_hour(self):
        loc = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] [class$=actual_class_time__value]')
        return json.loads(self.trim_text(loc))

    @allure.step('进入课程列表')
    def go_course_list(self):
        loc = (By.CSS_SELECTOR, '[role=tabpanel]:not([aria-hidden]) [class*=is-scrolling] [class$=actual_class_time__value]')
        self.poll_click(loc)
        return self

    @allure.step('关闭课程列表')
    def close_course_list(self):
        loc = (By.CSS_SELECTOR, '.el-dialog .el-icon-close')
        self.poll_click(loc)
        return self

    @allure.step('课程列表检索课程')
    def search_course(self, course_name: str = ''):
        search_input = (By.CSS_SELECTOR, 'input[placeholder*=课程名称]')
        self.clear_then_input(search_input, course_name)
        search_btn = (By.CSS_SELECTOR, '.el-dialog .search-button')
        self.poll_click(search_btn)
        time.sleep(1)
        return self

    @property
    @change_reset_implicit(implicit_timeout=2)
    @allure.step('获取课程列表检索匹配表单条数')
    def table_count_searched_course(self):
        loc = (By.CSS_SELECTOR, '.el-dialog [class*=is-scrolling] tr')
        return len(self.driver.find_elements(*loc))

    @change_reset_implicit(implicit_timeout=2)
    @allure.step('输入各课实际学时')
    def input_each_hour(self, hour):
        input_loc = (By.XPATH, '(//div[@role="dialog"]//*[contains(@class,"is-scrolling")]//input)[1]')
        self.element_click(input_loc)
        self.input_send_keys(input_loc,hour)
        # for ele, hour in tuple(zip(inputs, hour_list)):
        #     ele.clear()
        #     ele.send_keys(str(hour))
        #     sleep(1)
        return self

    @property
    @allure.step('获取课程列表显示总学时')
    def inner_total_hour(self):
        loc = (By.CSS_SELECTOR, '.el-dialog .classcourselist-headernotice *')
        self.move_to_click(loc)
        time.sleep(1)
        return json.loads(self.trim_text(loc))

    @allure.step('课程列表导出')
    def export_courses(self, file_name='课程列表.xlsx'):
        loc = (By.CSS_SELECTOR, '.el-dialog .ds-button[title=导出]')
        self.poll_click(loc)
        return wait_file_down_and_clean(file_name=file_name)
