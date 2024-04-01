from common.tools_packages import *


class HealthCondition(BasePage):
    status = ''  # 已提交或未提交学员列表状态

    @allure.step('检索班次')
    def search_class(self, class_name):
        self.locator_tag_search_input(placeholder='班次名称', value=class_name)
        self.locator_tag_search_button()
        return self

    @allure.step('导出班次列表')
    def export_classes(self):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        # export_confirm_btn = (
        #     By.XPATH, '//*[@aria-label="导出设置"]//*[contains(@class,"ds-button")]//*[contains(text(),"导出")]')
        # if self.judge_element_whether_existence(export_confirm_btn):
        #     self.element_click(export_confirm_btn)
        return wait_file_down_and_clean(file_name='班次列表.xlsx')

    @allure.step('进入未提交列表')
    def go_not_post_list(self, name):
        self.locator_view_value_click(header='未提交', id_value=name)
        self.status = '未提交'
        return self

    @allure.step('三高人员详情查询')
    def search_condition_stu(self, name):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name, times=2, enter=True)
        return self

    def search_stu(self, username: str):
        with allure.step(f'查询{self.status}学员'):
            self.locator_search_input(placeholder='姓名', value=username, enter=True, times=2)
        return self

    def export_stu_file(self):
        with allure.step(f'导出{self.status}学员列表'):
            self.locator_button(button_title='导出', dialog_title=' ')
            self.locator_dialog_btn(btn_name='确定')
        return wait_file_down_and_clean(file_name='学员列表.xlsx')

    @allure.step('进入已提交列表')
    def go_post_list(self, name):
        self.locator_view_value_click(header='已提交', id_value=name)
        self.status = '已提交'
        return self

    @allure.step('点击详情统计')
    def go_condition_list(self, name):
        self.locator_view_button(button_title='详情统计', id_value=name)
        return self

    @allure.step('三高详情列表检索')
    def search_condition(self, username):
        self.locator_search_input(placeholder='请输入姓名', value=username, enter=True, times=2)
        return self

    @allure.step('三高详情统计导出')
    def export_condition(self, tab_name):
        self.locator_tag_button(button_title='导出', dialog_title=' ')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name=f'{tab_name}-学员列表.xlsx')
