from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class SpecialUserAttendance(PersonnelSysPage):

    def _edit_info(self, data: dict):
        if '特殊考勤名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['特殊考勤名称'])
        if '考勤种类' in data:
            self.locator_select_list_value(ctrl_id='attend_type', value=data['考勤种类'])
        if '天数' in data:
            self.locator_text_input(ctrl_id='days', value=data['天数'])
        if '考勤人员' in data:
            name = data['考勤人员']
            self.locator_button(button_title='选择')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=name, enter=True)
            name_loc = (By.XPATH, f'//*[@ctrl_type="dsf.tree"]//*[contains(text(),"{name}")]'
                                  f'/../../..//*[@class="el-checkbox__input"]')
            self.excute_js_click(name_loc)
            self.locator_dialog_btn(btn_name='确定')
        if '开始生效时间' in data:
            data_input = (By.CSS_SELECTOR, '[form-name*="customattend_attend_person.begin_date"] input')
            self.input_readonly_js(data_input, value=data['开始生效时间'])
            self.element_click((By.XPATH, '//*[text()="特殊考勤人员设置"]'))
        if '删除人员' in data:
            del_btn = (By.XPATH, '//*[text()="%s"]/ancestor::tr//*[@title="删除"]' % (data['删除人员']))
            self.excute_js_click(del_btn)
            self.locator_dialog_btn(btn_name='确定')
        time.sleep(2)
        self.locator_button(button_title='保存')

    @allure.step('查询特殊考勤人员')
    def search_special_user(self, name):
        self.locator_tag_search_input(placeholder='考勤人员名称', value=name, enter=True)
        return self

    @allure.step('新增特殊考勤人员设置')
    def add_user_set(self, data):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self._edit_info(data)
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('编辑特殊考勤人员设置')
    def edit_user_set(self, name, data: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        self.locator_get_js_input_value(ctrl_id='name')
        self._edit_info(data)
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('删除特殊人员考勤设置')
    def del_user_set(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('删除特殊人员设置校验')
    def del_user_set_check(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        tip_loc = (By.CSS_SELECTOR, '.el-message-box__message p')
        info = self.get_ele_text_visitable(tip_loc)
        self.locator_dialog_btn(btn_name='确定')
        return info

    @allure.step('导出特殊考勤人员设置')
    def download_user_file(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='考勤生效列表.xlsx')
