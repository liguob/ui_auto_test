# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *


class MeetingInfo(BasePage):

    @allure.step('填写会议信息')
    def edit_info(self, data: dict):
        if '会议名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['会议名称'])
        if '会议类型' in data:
            self.locator_select_list_value(ctrl_id='type', value=data['会议类型'])
        if '会议开始时间' in data:
            self.locator_date_range(ctrl_id='duration', start_date=data['会议开始时间'], end_date=data['会议结束时间'])
        if '会议地点' in data:
            self.locator_search_magnifier(ctrl_id='addr')
            time.sleep(2)  # 等待元素加载
            site_info = data['会议地点']
            school_loc = (By.XPATH, f'//*[contains(text(),"{site_info[0]}")]')
            # 选择校区
            self.excute_js_click(school_loc)
            # 选择楼宇
            build_loc = (By.XPATH, f'//*[@role="treeitem"]//*[text()="{site_info[1]}"]')
            self.excute_js_click(build_loc)
            # 选择地点
            site_loc = (By.XPATH, f'//*[contains(text(),"{site_info[2]}")]')
            self.excute_js_click(site_loc)
            time.sleep(1)
            self.locator_dialog_btn(btn_name='确定')
        if '会议议程' in data:
            text_input = (By.XPATH, '//body[@contenteditable="true"]/p')
            edit_frame = (By.CSS_SELECTOR, 'iframe[id*="ueditor"]')
            self.switch_to_frame(loc=edit_frame)
            self.clear_and_input(text_input, value=data['会议议程'])
            self.switch_to_frame_back()
        if '与会领导' in data:
            self.locator_search_magnifier(ctrl_id='leaders')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=data['与会领导'], enter=True)
            self.locator_tree_node_click(node_value=data['与会领导'])
            self.locator_dialog_btn(btn_name='确定')
        if '参会人员' in data:
            self.locator_search_magnifier(ctrl_id='persons')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=data['参会人员'], enter=True)
            self.locator_tree_node_click(node_value=data['参会人员'])
            self.locator_dialog_btn(btn_name='确定')
        if '是否需要保障' in data:
            self.locator_select_radio(ctrl_id='have_guarantee', value=data['是否需要保障'])
        if '会议保障部门' in data:
            self.locator_search_magnifier(ctrl_id='guarantee_depts')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=data['会议保障部门'], enter=True)
            self.locator_tree_node_click(node_value=data['会议保障部门'])
            self.locator_dialog_btn(btn_name='确定')
        return self

    @allure.step('保存会议')
    def save_meeting(self):
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        self.close_and_return_page()
        from djw.page.smart_school_sys.后勤管理.会议管理.会议管理.meeting_manage import MeetingManage
        return MeetingManage(self.driver)

    @allure.step('发布会议')
    def push_meeting(self):
        self.locator_dialog_btn(btn_name='发布')
        self.wait_browser_close_switch_latest()
        from djw.page.smart_school_sys.后勤管理.会议管理.会议管理.meeting_manage import MeetingManage
        return MeetingManage(self.driver)
