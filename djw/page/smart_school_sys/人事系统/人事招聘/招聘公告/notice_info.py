# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *


class NoticeInfo(BasePage):
    """招聘公告信息填写页面"""

    @allure.step('编辑招聘公告信息')
    def edit_info(self, data):
        if "标题" in data:
            self.locator_text_input("title", data["标题"])
        if "开始时间" and "结束时间" in data:
            self.locator_date_range(ctrl_id="effective_date", start_date=data["开始时间"], end_date=data["结束时间"],
                                    confirm=True)
        if "年度" in data:
            self.locator_date(ctrl_id='year', value=data['年度'] + '年')
        if "正文" in data:
            textarea_iframe = (By.CSS_SELECTOR, 'iframe[id*=ueditor]')
            self.switch_to_frame(textarea_iframe)
            textarea = (By.CSS_SELECTOR, 'body.view')
            self.clear_and_input(textarea, data["正文"])
            self.switch_to_frame_back()
        if "附件" in data:
            self.locator_text_input("annex", data["附件"], is_file=True)
        time.sleep(2)  # 等待数据加载
        return self

    @allure.step('保存招聘公告')
    def save_notice(self):
        self.element_click((By.CSS_SELECTOR, '[title="保存"]'))
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()

    @allure.step('发布招聘公告')
    def push_notice(self):
        self.element_click((By.CSS_SELECTOR, '[title="发布"]'))
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
