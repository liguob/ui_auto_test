from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage
from common.tools_packages import *


class HomeworkReviewManagePage(EduManagePage):
    """作业批阅管理页"""

    @allure.step('查询作业')
    def search_homework(self, name):
        self.locator_tag_search_input(placeholder='班次名称、作业名称', value=name, times=2, enter=True)
        return self

    @allure.step('进入作业批阅详情页面')
    def go_review_detail(self, name):
        self.locator_view_button(button_title='批阅', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.班级管理.作业批阅.homework_review_detail import HomeworkReviewDetail
        return HomeworkReviewDetail(self.driver)
