# encoding=utf-8
"""
============================
Author:何凯
Time:2021/9/6 18:56
============================
"""
from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class RecruitNotice(PersonnelSysPage):
    """招聘公告页面类"""

    @allure.step('保存应聘导读')
    def save_recruit_text(self):
        self.locator_button(button_title="应聘导读")
        time.sleep(2)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        return self

    @allure.step('搜索招聘公告')
    def search_notice(self, value=' '):
        self.locator_search_input('标题/部门', value)
        self.locator_tag_search_button()
        return self

    @allure.step("点击新增公告")
    def click_add(self):
        self.locator_button("新增")
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.人事招聘.招聘公告.notice_info import NoticeInfo
        return NoticeInfo(self.driver)

    @allure.step('点击编辑公告')
    def click_edit(self, name):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.人事系统.人事招聘.招聘公告.notice_info import NoticeInfo
        return NoticeInfo(self.driver)

    @allure.step("取消发布招聘公告")
    def cancel_push_notice(self, name):
        self.locator_view_button(button_title="取消发布", id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('发布招聘公告')
    def push_notice(self, name):
        self.locator_view_button(button_title="发布", id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('删除招聘公告')
    def del_notice(self, name):
        self.locator_view_button(button_title="删除", id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self
