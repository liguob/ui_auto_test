# encoding=utf-8
"""
============================
Author:何超
Time:2021/4/16   11:20
============================
"""
import time

import allure
from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.教学资源.课程库管理.course_manage_page import CourseManagePage


class CourseSearchPage(CourseManagePage):
    """课程库查询页面"""
    menu_course_search = (By.XPATH, '//span[text()="课程库查询"]/parent::div')  # 课程库查询的菜单
    frame_page = (By.XPATH, '//iframe[@src="/dsfa/teas/zygl/kck/views/checklist.html"]')  # 课程库管理页面标题

    @allure.step("获取课程信息")
    def get_course_info_by_search(self):
        items = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[{}]')
        list_items = list(map(lambda x: (items[0], items[1].format(x)), range(2, 7)))
        try:
            title = ("课程名称", "教学形式", "课程类别", "使用范围", "填写日期")
            return self.publish_get_info(*list_items, title=title)
        except Exception:
            return ['']

    @allure.step("搜索课程")
    def search_course_by_search(self, course_name):
        return super().search_course(course_name)

    @allure.step("点击更多按钮")
    def click_btn_more_by_search(self):
        return super().click_btn_more()

    @allure.step("查看课程")
    def check_course_by_search(self):
        return super().check_course()
