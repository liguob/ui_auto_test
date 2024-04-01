# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/13    15:10
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.主页.home_page import HomePage


class EduSourcePage(HomePage):
    """教学资源页面"""

    @allure.step("进入场地库管理")
    def go_site_manage_page(self):
        self.locator_left_menu_click(button_title='场地库管理')
        from djw.page.smart_school_sys.教学资源.场地库管理.site_manage_main_page import SiteManageMainPage
        return SiteManageMainPage(driver=self.driver)

    @allure.step("进入基地库管理")
    def go_base_site_manage_page(self):
        self.locator_left_menu_click(button_title='基地库管理')
        from djw.page.smart_school_sys.教学资源.基地库管理.base_site_manage_page import BaseSiteManagePage
        return BaseSiteManagePage(driver=self.driver)

    @allure.step("进入基地库查询")
    def go_base_site_query_manage_page(self):
        self.locator_left_menu_click(button_title='基地库查询')
        from djw.page.smart_school_sys.教学资源.基地库查询.base_site_query_page import BaseSiteQueryPage
        return BaseSiteQueryPage(driver=self.driver)

    @allure.step("进入师资库管理")
    def go_teacher_manage_page(self):
        self.locator_left_menu_click(button_title='师资库管理')
        from djw.page.smart_school_sys.教学资源.师资库管理.teacher_data_management_page import TeacherDataManagePage
        self.wait_presence_list_data(explicit_timeout=20)
        return TeacherDataManagePage(driver=self.driver)

    @allure.step("进入资源占用一览表")
    def source_occupy_list_page(self):
        self.locator_left_menu_click(button_title='资源占用一览表')
        from djw.page.smart_school_sys.教学资源.资源占用一览表.source_occupation_list_page import SourceOccupyListPage
        return SourceOccupyListPage(driver=self.driver)

    @allure.step("进入师资库查询")
    def go_teacher_search_manage_page(self):
        self.locator_left_menu_click(button_title='师资库查询')
        from djw.page.smart_school_sys.教学资源.师资库查询.find_teacher_data_page import FindTeacherDatePage
        return FindTeacherDatePage(driver=self.driver)

    @allure.step('进入课程库管理')
    def go_course_manage_page(self):
        menu_btn = (By.XPATH, '//*[text()="课程库管理"]')
        menu = self.find_elms(menu_btn)
        if len(menu) == 4:
            menu[2].click()
            time.sleep(3)
        else:
            menu[0].click()
            time.sleep(3)
        from djw.page.smart_school_sys.教学资源.课程库管理.course_manage_page import CourseManagePage
        return CourseManagePage(driver=self.driver)

    @allure.step("进入课程库查询")
    def go_course_search(self):
        self.locator_left_menu_click(button_title='课程库查询')
        from djw.page.smart_school_sys.教学资源.课程库管理.course_search_page import CourseSearchPage
        return CourseSearchPage(driver=self.driver)

    @allure.step('进入案例库管理')
    def go_case_library_manage(self):
        self.locator_left_menu_click(button_title='案例库管理', times=1)
        from djw.page.smart_school_sys.教学资源.案例库管理.case_library_manage_page import CaseLibraryManagePage
        return CaseLibraryManagePage(driver=self.driver)

    @allure.step('进入教材库管理')
    def go_teaching_material_manage(self):
        self.locator_left_menu_click(button_title='教材库管理')
        from djw.page.smart_school_sys.教学资源.教材库管理.teaching_material_manage_page import TeachingMaterialPage
        return TeachingMaterialPage(self.driver)

    @allure.step('进入标签库管理')
    def go_tag_manage(self):
        self.locator_left_menu_click(button_title='标签库管理')
        from djw.page.smart_school_sys.教学资源.标签库管理.tag_lib_manage import TagLibManage
        return TagLibManage(self.driver)

    @allure.step('进入视频库管理')
    def go_video_manage(self):
        self.locator_left_menu_click(button_title='视频库管理')
        from djw.page.smart_school_sys.教学资源.视频库管理.video_manage import VideoManege
        return VideoManege(self.driver)

    @allure.step('进入课程标签')
    def go_course_tag(self):
        self.locator_left_menu_click(button_title='课程标签')
        from djw.page.smart_school_sys.教学资源.课程标签.course_tag import CourseTag
        return CourseTag(self.driver)
