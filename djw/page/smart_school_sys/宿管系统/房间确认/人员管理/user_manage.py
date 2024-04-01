from common.tools_packages import *


class UserManage(BasePage):

    def __init__(self, driver, team_name):
        super().__init__(driver=driver)
        self.team_name = team_name  # 团队名称

    @allure.step('查询人员')
    def search_user(self, name=''):
        self.locator_search_input(placeholder='姓名/身份证', value=name)
        self.locator_tag_search_button(dialog_title=self.team_name)
        return self

    def _edit_info(self, data: dict):
        if '人员姓名' in data:
            self.locator_text_input(ctrl_id='person_text', value=data['人员姓名'])
        if '身份证号码' in data:
            self.locator_text_input(ctrl_id='id_card', value=data['身份证号码'])
        if '联系方式' in data:
            self.locator_text_input(ctrl_id='phone', value=data['联系方式'])
        self.locator_dialog_btn('保存')

    @allure.step('新增人员')
    def add_user(self, data: dict):
        self.locator_button(dialog_title=self.team_name, button_title='新增')
        self._edit_info(data)
        self.wait_success_tip()
        return self

    @allure.step('编辑人员')
    def edit_user(self, name, data: dict):
        self.locator_view_button(button_title='编辑', dialog_title=self.team_name, id_value=name)
        self.locator_get_js_input_value(ctrl_id='person_text')
        self._edit_info(data)
        self.wait_success_tip()
        return self

    @allure.step('删除人员')
    def del_user(self, name):
        self.locator_view_button(button_title='删除', dialog_title=self.team_name, id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导入人员')
    def import_user(self, file):
        loc_btn = (By.CSS_SELECTOR, '[title="通用预导入"]')
        loc_input = (By.CSS_SELECTOR, '.to_desgin+input[type="file"]')
        self.upload_input_file(loc1=loc_btn, loc2=loc_input, file=file)
        self.wait_success_tip()
        return self

    @allure.step('人员导入模板下载')
    def download_model(self):
        self.locator_button(dialog_title=self.team_name, button_title='人员导入模板下载')
        return wait_file_down_and_clean(file_name='人员管理导入模板.xlsx')
