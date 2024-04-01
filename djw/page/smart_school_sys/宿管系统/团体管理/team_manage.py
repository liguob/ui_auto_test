# !/usr/bin/env python
# -*-coding:utf-8 -*-
from common.tools_packages import *
from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem


class TeamManage(RoomSystem):

    @allure.step('查询团体')
    def search_team(self, name=''):
        self.locator_search_input(placeholder='团体名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('删除选中的团体')
    def del_select_team(self):
        self.locator_button(button_title='删除')
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    def edit_info(self, data: dict):
        if '名称' in data:
            self.locator_text_input(ctrl_id='occupy_text', value=data['名称'])
        if '入住时间' in data:
            self.locator_date(ctrl_id='occupy_sdate', confirm=True, value=data['入住时间'])
        if '退房时间' in data:
            self.locator_date(ctrl_id='occupy_edate', confirm=True, value=data['退房时间'])
        if '预约信息' in data:
            with allure.step('添加预约信息'):
                self.locator_dialog_btn('添加预约记录')
                time.sleep(1)
                # 选择房间类型
                drop_list_btn = (By.CSS_SELECTOR, '[form-name*="dorm_room_reserve_detail.type"] input')
                self.excute_js_click(drop_list_btn)
                time.sleep(1)
                value = data['预约信息'][0]
                select_value = (By.XPATH, f"//*[@x-placement]//*[text()='{value}']")
                self.excute_js_click(select_value)
                # 输入房间数量
                input_value = (By.CSS_SELECTOR, '[form-name*="dorm_room_reserve_detail.total"] input')
                self.find_elem(input_value).send_keys(data['预约信息'][1])
        if '预约人员' in data:
            with allure.step('添加预约人员'):
                self.locator_button(button_title='添加预约人员')
                name_input = (By.XPATH, '//*[@ctrl-id="person"]//tbody//td[2]//input')  # 人员姓名
                self.find_elem(name_input).send_keys(data['预约人员'][0])
                id_input = (By.XPATH, '//*[@ctrl-id="person"]//tbody//td[3]//input')  # 身份证
                self.find_elem(id_input).send_keys(data['预约人员'][1])
                phone_input = (By.XPATH, '//*[@ctrl-id="person"]//tbody//td[4]//input')  # 联系方式
                self.find_elem(phone_input).send_keys(data['预约人员'][2])
                drop_list_btn = (By.XPATH, '//*[@ctrl-id="person"]//tbody//td[5]//input')  # 性别下拉框
                self.excute_js_click(drop_list_btn)
                time.sleep(1)
                sex_value = (By.XPATH, f"""//*[@x-placement]//*[text()="{data['预约人员'][3]}"]""")
                self.excute_js_click(sex_value)
                time.sleep(1)
        self.locator_button(button_title='保存')

    @allure.step('新增团队')
    def add_team(self, data: dict):
        self.locator_dialog_btn(btn_name='新增')
        self.edit_info(data)
        self.wait_success_tip()
        return self

    @allure.step('修改团队')
    def edit_team(self, name, data: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.edit_info(data)
        self.wait_success_tip()
        return self

    @allure.step('查看详情')
    def view_detail(self, name):
        self.locator_view_button(button_title='详情', id_value=name)
        time.sleep(2)
        name_value = (By.CSS_SELECTOR, '[ctrl-id="occupy_text"] [title]')
        info = self.get_text_implicitly(name_value)
        self.locator_dialog_btn('关闭')
        return info