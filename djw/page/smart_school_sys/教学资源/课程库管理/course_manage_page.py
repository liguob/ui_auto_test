# encoding=utf-8
"""
============================
Author:何超
Time:2021/4/16   11:20
============================
"""
import sys
import time
import allure
from selenium.webdriver.common.by import By
from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage
from common.decorators import change_reset_implicit
from common.file_path import wait_file_down_and_clean


class CourseManagePage(EduSourcePage):
    """课程库管理页面"""
    menu_course_manage = (By.XPATH, '//span[text()="课程库管理"]/parent::div')  # 课程库管理的菜单
    title_page = (By.XPATH, '//label[contains(text(),"课程列表")]')  # 页面标题
    course_export_btn = (By.CSS_SELECTOR, '.ds-button--icon-text[title=导出]')  # 课程库更多-导出按钮
    btn_import = (By.CSS_SELECTOR, '[module-name="teas.resource.course.manageList"] .ds-button-update')  # 课程库导入按钮

    course_more_btn = (By.CSS_SELECTOR, '.ds-button[title=更多]')  # 课程库更多按钮
    activity_more_btn = (By.CSS_SELECTOR, '[module-name="teas.resource.course.activity_list"] .ds-button__more')  # 活动库更多按钮

    course_search_input = (By.CSS_SELECTOR, '[module-name="teas.resource.course.manageList"] .search-input input')  # 课程检索框
    course_search_btn = (By.CSS_SELECTOR, '[module-name="teas.resource.course.manageList"] .search-button')  # 课程检索按钮
    activity_search_input = (By.CSS_SELECTOR, '[module-name="teas.resource.course.activity_list"] .search-input input')  # 活动检索框
    activity_search_btn = (By.CSS_SELECTOR, '[module-name="teas.resource.course.activity_list"] .search-button')  # 活动检索按钮

    edit_btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=编辑]')  # 课程/活动编辑按钮
    del_btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=删除]')  # 课程/活动删除按钮
    sealed_btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=封存]')  # 课程/活动封存按钮

    # 课程库查询库查看按钮
    view_btn = (By.CSS_SELECTOR, '[class*=is-scrolling] [title=查看]')

    btn_multiple_no = (By.XPATH, '//label[text()="教学形式:"]/following-sibling::div//button[contains(text(),"确定")]')  # 多选的取消按钮
    # 列表项
    tip = (By.XPATH, '//div[@class="layui-layer-content layui-layer-padding"]')  # 删除成功的提示
    # 编辑弹窗
    # frame_edit = (By.XPATH, '//iframe[contains(@src,"/dsfa/teas/zygl/kck/views/editxzkc.html")]')  # 编辑弹窗的frame
    text_title = (By.XPATH, '//div[@ctrl_type="Title2"]/label[text()="课程信息"]')  # 编辑窗口标题
    loading = (By.XPATH, '//div[@type="loading"]')  # 读取
    input_teach_form = (By.XPATH, '//label[text()="教学形式"]/following-sibling::div//input')  # 教学形式
    input_course_type = (By.XPATH, '//div[@caption="kclb"]//label[text()="课程类别"]/following-sibling::div//input')  # 课程类别
    input_near_teach_time = (By.XPATH, '//label[text()="最近授课时间"]/following-sibling::div//input')  # 最近授课时间
    input_subject_type = (By.XPATH, '//label[text()="学科分类"]/following-sibling::div//input')  # 学科分类
    input_class_object = (By.XPATH, '//label[text()="班次对象"]/following-sibling::div//input')  # 班次对象
    input_course_intro = (By.XPATH, '//label[text()="课程简介"]/following-sibling::div//textarea')  # 课程简介
    button_upload = (By.XPATH, '//label[text()="相关教案"]/following-sibling::div//span[text()="文件上传"]/parent::button')  # 文件上传按钮
    # 师资选择
    # frame_choice_box = (By.XPATH, '//iframe[contains(@src,"/dsfa/teas/zygl/szk/views/szxz.html")]')  # 师资弹窗的frame
    input_choice_box_no = (By.XPATH, '//div//span[text()="取消"]/parent::a')  # 选择弹窗的取消按钮
    # 查看弹窗
    list_course_key = (By.XPATH, '//table[@class="ds_table_layout_table"]//tr[@rowindex!="3"]//label[@class="layui-form-label"]')  # 课程信息标题
    list_course_value = (By.XPATH, '//table[@class="ds_table_layout_table"]//tr[@rowindex!="3"]//div[@class="layui-input-block"]')  # 课程信息

    @allure.step("点击更多按钮")
    def click_btn_more(self):
        self.excute_js_click_ele(self.course_more_btn)
        return self

    @allure.step("获取课程信息")
    def get_course_info(self):
        items = (By.XPATH, '//div[contains(@class,"is-scrolling")]//td[{}]')
        list_items = list(map(lambda x: (items[0], items[1].format(x)), range(3, 8)))
        try:
            title = ("课程名称", "授课教师", "教学形式", "课程类别", "使用范围")
            return self.publish_get_info(*list_items, title=title)
        except Exception as e:
            return ['']

    @allure.step("搜索课程")
    def search_course(self, course_name: str = ' '):
        self.locator_tag_search_input(placeholder='课程名称', value=course_name)
        self.locator_tag_search_button()
        self.wait_presence_list_data(explicit_timeout=20)
        return self

    @allure.step("查看课程")
    def check_course(self, index=1):
        from djw.page.smart_school_sys.教学资源.课程库管理.add_course_page import AddCoursePage
        time.sleep(0.5)
        self.excute_js_click_ele(self.view_btn)
        self.switch_to_handle()
        return AddCoursePage(self.driver)

    @allure.step("修改课程")
    def click_edit_course(self):
        from djw.page.smart_school_sys.教学资源.课程库管理.add_course_page import AddCoursePage
        self.excute_js_click_ele(self.edit_btn)  # 点击编辑按钮
        self.switch_to_handle(index=-1)
        return AddCoursePage(driver=self.driver)

    @allure.step("删除课程")
    def delete_course(self):
        btn_delete_yes = (By.XPATH, '//span[contains(text(),"确定")]/parent::button')  # 删除的确认按钮
        self.excute_js_click_ele(self.del_btn)  # 点击删除按钮
        self.excute_js_click_ele(btn_delete_yes)  # 点击提示窗口确认按钮
        return self

    @allure.step("点击新增课程")
    def go_add_course(self):
        """新增课程"""
        from djw.page.smart_school_sys.教学资源.课程库管理.add_course_page import AddCoursePage
        btn_add = (By.XPATH, '//a[@title="新增"]')  # 新增按钮
        self.element_click(btn_add)  # 点击新增按钮
        self.switch_to_handle()
        # self.switch_to_frame(AddCoursePage.frame)
        return AddCoursePage(self.driver)

    @allure.step("点击清空按钮")
    def clear(self):
        """编辑页面的清空"""
        btn_clear = (By.XPATH, '//div[@class="ds_sub_table_button_group"]//a[text()="清空"]')  # 清空按钮
        self.element_click(btn_clear)  # 点击清空按钮
        return self

    @allure.step("进入编辑课程页面并修改课程名称")
    def change_course(self):
        edit_page = self.click_edit_course()  # 点击修改按钮
        time.sleep(2)
        info = edit_page.add_course(teacher=False, use_scope='对外培训班')  # 修改课程名称
        time.sleep(1)
        edit_page.save_course()  # 保存
        self.switch_to_handle(index=-2)
        time.sleep(2)
        return info

    @allure.step('导入课程')
    def import_course(self, file):
        # self.locator_tag_button(button_title='预导入', file_path=file, times=3)
        self.locator_more_tip_button(button_title='预导入')
        time.sleep(1)
        self.element_click((By.XPATH, '//span[text()="导入数据"]'))
        # self._close_windows()
        self.find_elms((By.CSS_SELECTOR, 'input[type=file]'))[-1].send_keys(file)
        self.locator_dialog_btn(dialog_title='预导入文件编辑', btn_name='确定', times=1)
        self.wait_success_tip()
        return self

    @allure.step('异常导入课程')
    def import_course_error(self, file):
        # self.locator_tag_button(button_title='预导入', file_path=file, times=3)
        self.locator_more_tip_button(button_title='预导入')
        time.sleep(1)
        self.excute_js_click((By.XPATH, '//span[text()="导入数据"]'))
        self._close_windows()
        self.find_elms((By.CSS_SELECTOR, 'input[type=file]'))[-1].send_keys(file)
        self.locator_dialog_btn(dialog_title='预导入文件编辑', btn_name='确定', times=1)
        time.sleep(1)
        return self

    @allure.step('关闭课程导入浮页')
    def close_course_import_frame(self):
        close_btn = (By.XPATH, '//*[@role="dialog"]//*[@class="el-dialog__footer"]//*[contains(text(), "关闭")]')
        self.excute_js_click_ele(close_btn)
        time.sleep(1)

    @allure.step('导出课程')
    def export_course(self):
        self.click_btn_more()
        self.excute_js_click_ele(self.course_export_btn)
        return self

    @change_reset_implicit()
    @allure.step('判断是否需要导出确认')
    def judge_whether_export_confirm(self, filename):
        export_confirm_btn = (By.XPATH, '//*[@aria-label="导出设置"]//*[contains(@class,"ds-button")]//*[contains(text(),"导出")]')
        if self.judge_element_whether_existence(export_confirm_btn):
            self.element_click(export_confirm_btn)
        return wait_file_down_and_clean(filename)

    @property
    @change_reset_implicit()
    @allure.step('获取课程库(管理)列表检索表单结果条数')
    def table_searched_count(self):
        tr = (By.CSS_SELECTOR, '[class*=is-scrolling] tr')
        return len(self.driver.find_elements(*tr))

