# -*- coding: utf-8 -*-
"""
============================
@Time   :2021/11/18 14:58
@Author :李国彬
============================
"""
from common.tools_packages import *
from common.base_page import BasePage


class StuManageInfoPage(BasePage):
    """班主任-学员管理页面"""

    @allure.step("点击确定")
    def __click_confirm(self):
        confirm_btn = (By.XPATH, '//span[contains(text(),"确定")]')  # 确定
        self.excute_js_click(confirm_btn)
        return self

    @allure.step("切换到在校学员")
    def switch_in_school_stu(self):
        in_school_tab = (By.XPATH, '//div[@role="tab"]//*[contains(text(),"在校学员")]')  # 在学学员页签
        self.excute_js_click(in_school_tab)
        # 等待页面短暂刷新
        sleep(1)
        return self

    @allure.step("切换到未报到")
    def switch_no_report(self):
        no_report_tab = (By.XPATH, '//div[@role="tab"]//*[contains(text(),"未报到")]')  # 未报到页签
        self.excute_js_click(no_report_tab)
        # 等待页面短暂刷新
        sleep(1)
        return self

    @allure.step("切换到退学")
    def switch_no_finish(self):
        no_finish_tab = (By.XPATH, '//div[@role="tab"]//*[contains(text(),"退学")]')  # 退学页签
        self.excute_js_click(no_finish_tab)
        # 等待页面短暂刷新
        sleep(1)
        return self

    @allure.step("切换到跟班人员")
    def switch_follow_class(self):
        follow_class_tab = (By.XPATH, '//div[@role="tab"]//*[contains(text(),"跟班人员")]')  # 跟班人员页签
        self.excute_js_click(follow_class_tab)
        # 等待页面短暂刷新
        sleep(1)
        return self

    @allure.step("查询学员")
    def search_stu(self, name=""):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step("在校学员置为退学")
    def stu_set_no_finish(self, name, values: dict):
        """根据学员名称操作"""
        keys = values.keys()
        # 退学按钮
        self.locator_view_button(id_value=name, button_title='退学')
        reason = (By.CSS_SELECTOR, '[role=dialog] [ctrl-id=reason] textarea')  # 退学事由
        select_date = (By.CSS_SELECTOR, '[role=dialog] [ctrl-id=leave_date] input')  # 退学时间
        file = (By.CSS_SELECTOR, '[role=dialog] [ctrl-id=attachment] input')  # 退学附件
        if "退学事由" in keys:
            self.input_send_keys(reason, values["退学事由"])
        if "退学时间" in keys:
            self.input_readonly_js(select_date, values["退学时间"])
            self.move_to_click(reason)
        if "退学附件" in keys:
            self.input_readonly_js(file, values["退学附件"])
        self.locator_dialog_btn("保存")
        self.__click_confirm()
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step("在校学员置为未报到")
    def stu_set_no_report(self, name):
        """根据学员名称操作"""
        self.locator_view_button(button_title='未报到', id_value=name)
        self.__click_confirm()
        self.wait_success_tip()
        return self

    @allure.step("勾选学员")
    def select_stu(self, name):
        # 勾选按钮
        self.locator_view_select(id_value=name)
        return self

    @allure.step("修改学员是否优秀学员状态")
    def stu_set_excellent(self, name):
        """当前使用全选按钮，学员名称操作"""
        click_btn = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//div[@role="switch"]')
        self.search_stu(name)
        self.excute_js_click(click_btn)
        self.wait_success_tip()
        sleep(2)
        return self

    @allure.step('获取是否优秀学员状态')
    def get_excellent_status(self, name):
        text_ele = (By.XPATH, f'//*[text()="{name}"]/ancestor::tr//span[contains(@class,"is-active")]/span')
        return self.find_elem(text_ele).text

    def del_stu(self, stu_name, status):
        with allure.step(f'删除{status}学员'):
            self.locator_view_button(button_title='删除', id_value=stu_name)
            self.locator_dialog_btn('确定')
            self.wait_success_tip()
        return self

    @allure.step("未报到设为在校")
    def no_report_stu_set_in_school(self, name):
        """根据学员名称操作"""
        self.search_stu(name)
        self.locator_view_button(button_title='在校', id_value=name)
        self.__click_confirm()
        self.wait_success_tip()
        return self

    @allure.step("新增学员")
    def add_stu(self, values: dict):
        """新增学员并关闭界面"""
        self.locator_tag_button(button_title='新增')
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_student_page import ClassManageEditStudentPage
        ClassManageEditStudentPage(self.driver).edit_student_info(values)
        # 等待新增学员窗口关闭
        self.wait_browser_close_switch_latest()
        return self

    @allure.step("新增学员校验")
    def add_stu_fail(self, values: dict = None):
        self.locator_tag_button(button_title='新增')
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_student_page import ClassManageEditStudentPage
        return ClassManageEditStudentPage(self.driver).edit_student_fail(values)

    @allure.step("修改学员")
    def edit_stu(self, name, values: dict):
        self.locator_view_button(button_title='编辑', id_value=name)
        self.wait_open_new_browser_and_switch()
        # 等待接口数据返回
        sleep(3)
        # 进入编辑页面frame
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_student_page import ClassManageEditStudentPage
        ClassManageEditStudentPage(self.driver).edit_student_info(values)
        # 等待窗口关闭学员信息页面
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('导入学员')
    def import_student(self, file):
        self.locator_more_tip_button(button_title='预导入')
        self.locator_dialog_btn(btn_name='导入数据')
        sleep(0.5)
        input_loc = (By.CSS_SELECTOR, 'input[type="file"][accept*="vnd.ms-excel"]')
        self.find_elem(input_loc).send_keys(file)
        time.sleep(3)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('导入学员照片')
    def import_stu_image(self, zip_file_path: str):
        self.locator_more_tip_button(button_title='图片命名规则：姓名  导入格式：zip文件', file_path=zip_file_path)
        return self.wait_success_tip()

    @allure.step('导入学员校验')
    def import_student_check(self, file):
        self.locator_more_tip_button(button_title='预导入')
        time.sleep(2)
        self.locator_dialog_btn(btn_name='导入数据')
        input_loc = (By.CSS_SELECTOR, 'input[type="file"][accept*="vnd.ms-excel"]')
        self.find_elem(input_loc).send_keys(file)
        time.sleep(3)
        self.locator_dialog_btn(btn_name='确定')
        return self.get_all_required_prompt()

    @allure.step('学员照片导出')
    def export_stu_pic(self, class_name):
        self.locator_more_tip_button('照片导出')
        return wait_file_down_and_clean(f'{class_name}-学员照片.zip')

    @allure.step('打印入学通知书')
    def print_school_book(self):
        self.locator_more_tip_button('打印入学通知')
        return wait_file_down_and_clean('学员入学通知书.doc')

    @allure.step('重置密码')
    def reset_pwd(self):
        self.locator_more_tip_button('重置密码')
        self.locator_dialog_btn('确定')
        return self.wait_success_tip()
