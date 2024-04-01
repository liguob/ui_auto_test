# !/usr/bin/env python
# -*-coding:utf-8 -*-

from common.tools_packages import *


class CarInfoEdit(BasePage):

    @allure.step('编辑用车申请信息')
    def edit_apply_info(self, values: dict):
        if '用车人' in values:
            self.locator_search_magnifier(ctrl_id='vehicle_user')
            time.sleep(2)
            self.locator_search_input(placeholder='输入关键字进行过滤', value=values['用车人'], enter=True)
            self.locator_tree_node_click(node_value=values['用车人'])
            self.locator_dialog_btn(btn_name='确定')
        if '用车开始时间' in values:
            self.locator_date_range(ctrl_id='use', start_date=values['用车开始时间'], end_date=values['用车结束时间'])
        if '联系电话' in values:
            self.locator_text_input(ctrl_id='phone', value=values['联系电话'])
        return self

    @allure.step('保存用车申请')
    def save_apply(self):
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        from djw.page.smart_school_sys.后勤管理.车辆管理.用车申请.car_apply import CarApply
        return CarApply(self.driver)

    @allure.step('发送用车申请')
    def push_apply(self, name):
        self.locator_button(button_title='发送')
        # 判断是否有选择办理人弹窗信息
        dialog_ele = (By.CSS_SELECTOR, '[aria-label="请选择办理人"]')
        if self.find_elements_no_exception(dialog_ele):
            self.locator_search_input(placeholder='输入名称', value=name, times=3)
            select_name = (By.XPATH, f'//*[text()="{name}"]')  # 教研领导是教研审核的登录角色名称
            self.excute_js_click(select_name)
            self.locator_dialog_btn('确定')
            self.wait_browser_close_switch_latest(times=5)
        else:
            self.switch_to_window(-1)
        return self
