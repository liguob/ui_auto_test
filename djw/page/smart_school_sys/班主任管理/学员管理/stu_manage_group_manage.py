# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/5/17    13:53
============================
学员管理-分组管理页面
"""
import time
from time import sleep

import allure
from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.主页.home_page import HomePage


class StudentGroupManagePage(HomePage):

    @allure.step("进入未分组")
    def switch_to_no_group(self):
        click_ele = (By.XPATH, '//div[@role="tablist"]//*[contains(text(),"未分组")]')
        self.excute_js_click(click_ele)
        sleep(1)  # 切换分组时短暂的加载时间
        return self

    @allure.step("进入已分组")
    def switch_to_have_group(self):
        click_ele = (By.XPATH, '//div[@role="tablist"]//*[contains(text(),"已分组")]')
        self.excute_js_click(click_ele)
        sleep(1)  # 切换分组时短暂的加载时间
        return self

    @allure.step("创建小组")
    def create_group(self, num):
        create_btn = (By.CSS_SELECTOR, 'a[ds-event=ctegroup]')  # 点击创建小组
        input_ele = (By.CSS_SELECTOR, 'input.layui-layer-input')  # 小组数量
        self.excute_js_click(create_btn)
        self.clear_and_input(input_ele, num)

    @allure.step("选择班次或组名")
    def select_name(self, name):
        """选择左侧的班次或组名"""
        name_ele = (By.XPATH, '//div[@role="tree"]//span[text()="{}"]'.format(name))
        self.excute_js_click(name_ele)
        sleep(2)  # 点击后会重新加载页面
        return self

    @allure.step("创建小组")
    def add_group(self, num):
        self.locator_button(button_title="创建小组")
        self.locator_search_input(placeholder='请输入整数', value=num)
        self.locator_dialog_btn('确定')
        time.sleep(1)
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    def __handle_grouping(self, group_name):
        self.locator_tag_button(button_title='分配小组')
        sleep(2)
        self.locator_select_list_value(ctrl_id='group', value=group_name)
        self.locator_button(button_title='分配')
        self.locator_dialog_btn('确定')
        self.wait_success_tip()
        return self

    @allure.step("小组手动分配学员")
    def group_handle_grouping(self, group_name):
        self.__handle_grouping(group_name)
        return self

    @allure.step('按学号分组')
    def auto_group_by_stu_num(self):
        loc1 = (By.CSS_SELECTOR, '[title="自动分组"]')
        loc2 = (By.XPATH, '//*[@aria-hidden="false"]//*[contains(text(), "按学号")]')
        self.move_and_move_to_click(loc1, loc2)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(1)
        return self

    @allure.step("按性别自动分组")
    def auto_grouping_by_sex(self):
        loc1 = (By.CSS_SELECTOR, '[title="自动分组"]')
        loc2 = (By.XPATH, '//*[@aria-hidden="false"]//*[contains(text(), "自定义条件")]')
        self.move_and_move_to_click(loc1, loc2)
        rule_name_btn = (By.CSS_SELECTOR, 'div[ctrl-id=groupsort] input[type=text]')  # 规则名选择按钮
        rule_sex = (By.XPATH, '//div[@x-placement]//*[contains(text(),"性别")]')  # 性别
        sleep(1)  # 等待加载
        # 等待界面加载完成
        self.locator_button(button_title='添加条件')
        self.excute_js_click(rule_name_btn)
        self.excute_js_click(rule_sex)
        self.locator_button('分组')
        self.locator_dialog_btn('确定')
        return self.wait_success_tip()

    def __del_group(self, name):
        """执行删除小组操作"""
        self.locator_more_tip_button(button_title='删除分组')
        self.locator_select_list_value(ctrl_id='group', value=name)
        self.locator_dialog_btn('删除')
        self.locator_dialog_btn('确定')

    def __get_tip_info(self):
        """获取提示信息文本"""
        return self.get_ele_text_visitable(self.__tip_info)

    @allure.step("删除分组")
    def del_group(self, name):
        self.__del_group(name)
        # 操作后界面自动刷新等待
        sleep(2)
        return self

    @allure.step("删除分组校验")
    def def_group_fail(self, name):
        self.__del_group(name)
        return self.__get_tip_info()

    @allure.step("新增学员")
    def add_stu(self, data: dict):
        self.locator_button(button_title='更多')
        self.locator_button(button_title='新增学员')
        self.switch_to_window(-1)
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_edit_student_page import \
            ClassManageEditStudentPage
        ClassManageEditStudentPage(self.driver).edit_student_info(data)
        self.switch_to_window(-2)
        self.refresh()
        return self

    @allure.step("编辑小组")
    def edit_group(self, name):
        self.locator_more_tip_button(button_title='编辑分组')
        sleep(2)  # 等待元素值值加载完成，否则可能原有值未能清空
        self.locator_text_input(ctrl_id='zmc', value=name)
        self.locator_dialog_btn("保存")
        self.wait_success_tip()
        return self

    @allure.step("获取分组名称")
    def get_groups_name(self):
        self.switch_to_frame_back()
        name_ele = (By.CSS_SELECTOR, '.tree-name i+span')
        elements = self.find_elms(name_ele)
        return [i.text for i in elements]

    def __select_all_stu(self):
        click_ele = (By.CSS_SELECTOR, 'table.el-table__header label')  # 全选按钮
        self.excute_js_click(click_ele)

    @allure.step("勾选班次全部学员")
    def select_class_all_stu(self):
        self.__select_all_stu()
        return self

    @allure.step("勾选小组全部学员")
    def select_group_all_stu(self):
        self.__select_all_stu()
        return self
