# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/3/25    13:47
============================
"""
import time
import allure
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class ClassManageEditClassPage(BasePage):
    """班次管理-班次管理信息页面"""
    __tip_info = (By.CSS_SELECTOR, 'div.ds-error-text')  # 提示信息
    # 以下为班次管理-基础信息
    __save_class_btn = (By.CSS_SELECTOR, '[title="保存"].ds-button')  # 班次信息保存

    @allure.step("填写班次信息")
    def __edit_class_info(self, values: dict):
        """进入班次修改页面，并填写信息后保存"""
        keys = values.keys()
        # 滚动使页面元素其加载
        # self.move_to_ele(self.__save_class_btn)
        if "调学人数" in keys:
            # 选择单位
            self.__select_unit(values['调学人数'])
        if "班主任" in keys:
            self.__select_master(values["班主任"])
        if "班次名称" in keys:
            self.locator_text_input('name', values["班次名称"])
        if "班次分类" in keys:
            self.locator_select_list_value('bclx', values["班次分类"], wait_time=1)
        if "学期" in keys:
            self.locator_select_radio('xq', values["学期"])
        if "学年" in keys:
            self.locator_text_input(ctrl_id='school_year', value=values["学年"], is_readonly=True)
        if "培训开始时间" in keys:
            self.locator_date_range('pxsj', values["培训开始时间"], values["培训结束时间"])
        if "计划人数" in keys:
            self.locator_text_input('jhrs', values["班次名称"])
        if "培训形式" in keys:
            # 培训形式
            self.locator_select_radio('type', values["培训形式"])
        if "启用状态" in keys:
            # 启用状态
            self.locator_select_radio('qyzt', values["启用状态"])
        #   网报信息
        if "网报形式" in keys:
            self.locator_select_radio('enroll_type', values["网报形式"])
        if "网报费用" in keys:
            self.locator_text_input('wbfy', values["网报费用"])
        if "上课地点" in keys:
            self.locator_search_magnifier(ctrl_id='skdd')
            time.sleep(2)  # 等待元素加载
            site_info = values['上课地点']
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
        if "网报开始时间" in keys:
            self.locator_date_range(ctrl_id='wbsj', start_date=values["网报开始时间"], end_date=values["网报结束时间"],
                                    )
        time.sleep(2)  # 等待数据加载，避免点击保存失效

    def edit_class_info(self, values: dict):
        """班次信息填写"""
        self.__edit_class_info(values=values)
        self.locator_button(button_title='保存')
        self.wait_success_tip()
        self.close_and_return_page()
        return self

    def edit_class_info_fail(self, values: dict):
        """校验班次信息返回提示信息"""
        self.__edit_class_info(values)
        self.excute_js_click(self.__save_class_btn)
        return self.get_all_required_prompt()

    @allure.step("选择班主任")
    def __select_master(self, name):
        """基础信息中查询，并选择班主任"""
        master_search_btn = (By.CSS_SELECTOR, '[ctrl-id="bzr"] i')  # 进入班主任选择界面按钮
        save_btn = (By.XPATH, '//span[text()="确定"]')  # 确定按钮
        # 进入班主任选择界面
        self.element_click(master_search_btn)
        time.sleep(3)
        # 查询班主任
        self.locator_search_input(placeholder='输入关键字进行过滤', times=1, value=name, enter=True)
        # 选择班主任
        self.locator_tree_node_click(node_value=name)
        self.find_elem(save_btn).click()
        return self

    @allure.step("保存调训单位")
    def __select_unit(self, name):
        """根据单元名称name调学人数中选择单位"""
        # 进入新增的浏览器页面
        with allure.step("进入调学人数界面"):
            online_adjust_class_btn = (By.CSS_SELECTOR, 'div[ctrl-id=txrs] span')  # 调学人数点击
            self.excute_js_click(online_adjust_class_btn)
            self.wait_open_new_browser_and_switch()
        with allure.step("进入单位选择界面"):
            self.locator_button(button_title='选择')
        with allure.step("选择单位"):
            """查询单位后选择单位"""
            # 先查询后选择
            self.locator_search_input(placeholder='输入关键字进行过滤', value=name, enter=True)
            self.locator_tree_node_click(node_value=name)
            time.sleep(1)
            self.locator_dialog_btn('确定')
            time.sleep(1)
        # 保存切换窗口
        self.locator_button(button_title='保存')
        self.wait_browser_close_switch_latest()
        return self

    @allure.step("保存选择单位")
    def select_unit(self):
        self.find_elem(self.__save_class_btn).click()
        # 返回到班次管理页面（此时应有二个页面，返回第二个）
        self.switch_to_window(1)
        return self

    @allure.step('切换到学员管理')
    def switch_student_manage(self):
        self.locator_switch_tag(tag_name='学员管理')
        from djw.page.smart_school_sys.教务管理.教学管理.班次管理.班次管理.class_manage_student_page import ClassMangeStudentPage
        return ClassMangeStudentPage(self.driver)
