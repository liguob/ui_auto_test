# encoding=utf-8
"""
============================
Author:何超
Time:2021/4/26   13:30
============================
"""
import time
from collections import namedtuple
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.base_page import BasePage
from common.random_tool import randomTool
from common.file_path import wait_file_down_and_clean
from common.decorators import change_reset_implicit


class DrawTeachPlanPage(BasePage):
    """制定教学计划"""

    add_btn = (By.CSS_SELECTOR, '.plan-content [data-index="0"] .icon-hao')  # 悬浮新增按钮
    frame = (By.XPATH, '//iframe[@class="page-head-font-fixed"]')
    loading = (By.XPATH, '//div[contains(@class,"layui-layer layui-layer-loading")]')  # 进度条
    text_title = (By.XPATH, '//div[@class="teach_plan_top_title"]')  # 页面标题
    # 复制教学计划
    frame_copy_teach_plan = (By.XPATH, '//iframe[contains(@src,"/dsfa/teas/jwgl/jxjh/views/chooseClass.html")]')
    btn_teach_plan_no = (By.XPATH, '//div[@class="layui-layer-btn layui-layer-btn-"]/a[2]')  # 取消按钮

    module1 = (By.XPATH, '(//div[@class="teach_plan_title"])[1]')  # 版块1
    # 新增模块
    btn_back = (By.XPATH, '//div[contains(@class,"teach_plan_module_high")]//div[@class="teach_plan_edit_box_back blue"]')  # 返回按钮
    btn_delete = (By.XPATH, '//div[contains(@class,"teach_plan_module_high")]//div[@class="teach_plan_edit_box_del red"]')  # 删除按钮
    btn_module_move = (By.XPATH, '//div[contains(@class,"teach_plan_module_top_bg")]//i[contains(@class,"template")]')  # 层级

    btn_hidden_show_content = (By.CSS_SELECTOR, '.row-right [class*=shuangjiantou]~*')  # 隐藏/显示目录按钮
    all_unfold = (By.XPATH, '//*[contains(@class, "row-right")]//*[contains(text(), "全部展开")]')  # 全部展开按钮
    all_fold = (By.XPATH, '//*[contains(@class, "row-right")]//*[contains(text(), "全部折叠")]')  # 全部折叠按钮
    left_content = (By.CSS_SELECTOR, '[class=teach_plan_left_box]')  # 是否显示左侧目录
    course_teacher_plan_mould_search_input = (By.CSS_SELECTOR, '.search-input input')  # 选择课程/教师/计划/模板页搜索框
    course_teacher_plan_mould_search_btn = (By.CSS_SELECTOR, '.search-button')  # 选择课程/教师/计划/模板页检索按钮
    checkbox = (By.CSS_SELECTOR, '.is-scrolling-none .el-checkbox__inner')  # 课程/教师/计划/模板检索列表数据复选框
    confirm_btn = (By.XPATH, '//*[contains(@class, "ds-button")]//*[contains(text(), "确定")]')  # 模板/计划课程/教师检索列表确定按钮
    continue_btn = (By.XPATH, '//*[@class="el-message-box__btns"]//*[contains(text(),"继续")]')  # 选择模板/复制教学计划覆盖提示弹窗继续按钮

    no_content = (By.CSS_SELECTOR, '.el-tree__empty-text')  # 暂无数据

    @allure.step("获取制定教学计划页面标题")
    def get_draw_teach_plan_title(self):
        self.wait_visibility_ele(self.text_title)
        title = self.trim_text(self.text_title)
        handle_title = self.driver.title
        value = namedtuple('title', ['page_title', 'handle_title'])
        return value(title, handle_title)

    @allure.step('点击隐藏目录按钮')
    def click_hidden_left_content(self):
        self.poll_click(self.btn_hidden_show_content)
        return self

    @allure.step('点击显示目录按钮')
    def click_show_left_content(self):
        self.poll_click(self.btn_hidden_show_content)
        return self

    @allure.step('校验点击隐藏目录')
    def msg_click_hidden_left_content(self):
        exist_left_content = self.is_element_exist(self.left_content)  # 预期为False
        btn_text = self.alert_tip(keyword='显示目录', loc=self.btn_hidden_show_content)  # 预期文本为显示目录
        Res = namedtuple('Res', ['exist_left_content', 'btn_text'])
        return Res(exist_left_content, btn_text)

    @allure.step('校验点击显示目录')
    def msg_click_show_left_content(self):
        exist_left_content = self.is_element_exist(self.left_content)  # 预期为True
        btn_text = self.alert_tip(keyword='隐藏目录', loc=self.btn_hidden_show_content)  # 预期文本为隐藏目录
        Res = namedtuple('Res', ['exist_left_content', 'btn_text'])
        return Res(exist_left_content, btn_text)

    @allure.step("点击班级课表按钮")
    def click_class_schedule(self):
        time.sleep(2)
        btn_class_schedule = (By.CSS_SELECTOR, '.row-right [class*=yzkb]~*')  # 班级课表按钮
        self.poll_click(btn_class_schedule)
        time.sleep(1)
        self.switch_to_handle(index=-1)
        return self

    @property
    @allure.step("获取跳转班级课表页的url")
    def class_schedule_url(self):
        return self.driver.current_url

    @allure.step('点击全部展开')
    def click_all_unfold(self):
        self.excute_js_click_ele(self.all_unfold)
        time.sleep(0.5)
        return self

    @allure.step('点击全部折叠')
    def click_all_fold(self):
        self.excute_js_click_ele(self.all_fold)
        time.sleep(0.5)
        return self

    @allure.step('展开更多下拉菜单')
    def expand_more(self):
        more_arrow = (By.XPATH, '//*[contains(text(), "更多")]//*[contains(@class, "el-icon--right")]')
        self.poll_click(more_arrow)
        time.sleep(0.5)
        return self

    @allure.step('选择更多下拉选项')
    def choice_more_option(self, option):
        more_option = (By.XPATH, f'//*[@class="el-dropdown-menu__item" and contains(text(), "{option}")]')  # 更多下拉选项
        self.excute_js_click_ele(more_option)
        return self

    @allure.step('选择模板')
    def choose_existed_mould(self, mould_name):
        self.expand_more().choice_more_option(option='选择模板')
        self.locator_search_input(placeholder='请输入模版名称', value=mould_name, enter=True)
        self.locator_view_select(id_value=mould_name)
        self.locator_dialog_btn(btn_name='确定')
        self.locator_dialog_btn(btn_name='继续')
        return self

    @allure.step('复制教学计划')
    def copy_existed_plan(self, class_name):
        self.expand_more().choice_more_option(option='复制教学计划')
        self.locator_switch_tag(tag_name='未开始', dialog_title='选择教学计划')
        self.locator_tag_search_input(placeholder='请输入名称', value=class_name, dialog_title='选择教学计划')
        self.locator_tag_search_button(dialog_title='选择教学计划')
        # self.clear_then_input(self.course_teacher_plan_mould_search_input, class_name)
        # self.excute_js_click_ele(self.course_teacher_plan_mould_search_btn)
        time.sleep(0.5)
        self.excute_js_click_ele(self.checkbox)
        time.sleep(0.5)
        self.excute_js_click_ele(self.confirm_btn)
        self.excute_js_click_ele(self.continue_btn)

    @allure.step('导出(教学计划)')
    def export_plan(self, class_name):
        """class_name: 导出教学计划的班次名称"""
        self.expand_more().choice_more_option(option='导出')
        return wait_file_down_and_clean(f'{class_name}.doc')

    @allure.step('导出教学计划模板')
    def export_mould(self, mould_name):
        """mould_name: 教学计划模板名称"""
        export_mould_btn = (By.XPATH, '//*[contains(@class, "row-right")]//*[contains(text(), "导出")]')
        self.excute_js_click_ele(export_mould_btn)
        return wait_file_down_and_clean(f'{mould_name}.doc')

    @allure.step('预览教学计划')
    def preview_plan(self):
        self.expand_more().choice_more_option(option='预览')
        time.sleep(3)  # 等待预览标签页打开
        self.switch_to_handle(index=2)
        return self

    @allure.step('预览教学计划模板')
    def preview_mould(self):
        preview_mould_btn = (By.XPATH, '//*[contains(@class, "row-right")]//*[contains(text(), "预览")]')
        self.excute_js_click_ele(preview_mould_btn)
        time.sleep(3)  # 等待预览标签页打开
        self.switch_to_handle(index=2)
        return self

    @property
    @change_reset_implicit(1)
    @allure.step('预览教学计划/教学计划模板内容断言')
    def preview_contents(self):
        preview_content = (By.XPATH, '//body//embed[@name!="" and @internalid!=""]')
        contents = self.driver.find_elements(*preview_content)
        return contents

    @property
    @allure.step('是否暂无数据')
    def had_content(self):
        return self.is_element_exist(self.no_content)

    @allure.step('将当前计划设为模板')
    def set_to_mould(self, mould_name):
        set_mould_btn = (By.XPATH, '//*[contains(@class, "row-right")]//*[contains(text(), "设为模板")]')
        name_input = (By.CSS_SELECTOR, '[aria-label=设为模板] input')  # 设为模板-模板名称输入框
        save_btn = (By.CSS_SELECTOR, '[aria-label=设为模板] .ds-button:not([title=关闭])')  # 设为模板-保存按钮
        self.excute_js_click_ele(set_mould_btn)
        self.clear_then_input(name_input, mould_name)
        time.sleep(0.5)
        self.poll_click(save_btn)
        time.sleep(0.5)
        self.explicit_wait_ele_presence(self.WEB_TIP)
        return self

    @allure.step("点击复制教学计划")
    def click_copy_teach_plan(self):
        btn_copy_plan = (By.XPATH, '//button[text()="复制教学计划"]')  # 复制计划按钮
        self.wait_ele_be_click(btn_copy_plan)
        self.excute_js_click(btn_copy_plan)
        self.switch_to_frame_back()
        self.switch_to_frame(self.frame_copy_teach_plan)
        return self

    @allure.title('输入板块和课程模块标题')
    def set_section_course_module_title(self):
        input_loc = (By.CSS_SELECTOR, '[validatekey*="teaching_plan_detail.title"] [placeholder]')
        inputs = self.driver.find_elements(*input_loc)
        for i in inputs:
            i.send_keys(randomTool.random_str())
            time.sleep(0.5)
        # section_title_input, course_module_title_input = inputs[0], inputs[1]
        # section_title_input.send_keys(randomTool.random_str()+'\n')
        # time.sleep(0.25)
        # course_module_title_input.send_keys(randomTool.random_str()+'\n')
        # time.sleep(0.25)
        return self

    @allure.title('点击全部保存')
    def save_all(self):
        self.element_click((By.XPATH, '//*[contains(text(), "全部保存")]'))
        return self.wait_success_tip()

    @allure.step("点击新增板块")
    def click_add_section(self):
        btn_add_section = (By.XPATH, '//*[contains(@class, "row-right")]//*[contains(text(), "新增板块")]')
        self.poll_click(btn_add_section)
        self.mouse_hover_to_ele(btn_add_section)
        return self

    @allure.title('新增课程计划')
    def add_course_plan(self, course_name=' '):
        self.click_add_section()  # 新增板块
        time.sleep(1)
        self.add_course_module(module_name="普通模块")  # 新增课程模块
        time.sleep(0.5)
        self.set_course(course_name)  # 设置课程
        time.sleep(0.5)
        return self

    @allure.title('新增课程模块')
    def add_course_module(self, module_name="课程模块"):
        select_module = (By.XPATH, f'//*[@x-placement]//*[@class="el-dropdown-menu__item" and contains(text(), "{module_name}")]')
        self.element_click(select_module)
        add_btns = self.driver.find_elements(*self.add_btn)
        first_add_btn = add_btns[0]
        self.excute_js_click_ele(first_add_btn)
        course_module = (By.XPATH, '//*[@x-placement]//*[@class="el-dropdown-menu__item" and contains(text(), "课程模块")]')
        self.excute_js_click_ele(course_module)
        return self

    @allure.title('进入课程选择表单')
    def into_course_select(self):
        go_add_course_btn = (By.XPATH, '//*[@class="table-div-btns"]//*[contains(text(), "新增课程")]')  # 课程模块-新增课程按钮
        self.poll_click(go_add_course_btn)
        # course_module_search_btn = (By.XPATH, '//*[contains(@class, "is-scrolling")]//*[contains(@class, "el-icon-search")]')  # 课程模块内放大搜索按钮
        # course_module_search_btns = self.driver.find_elements(*course_module_search_btn)
        # into_course_btn = course_module_search_btns[0]
        # self.excute_js_click_ele(into_course_btn)
        return self

    @allure.title('设置课程')
    def set_course(self, course_name=' '):
        """进入课程选择表单-搜索课程->勾选->确定"""
        self.into_course_select()  # 进入课程选择表单
        self.locator_search_input(placeholder='课程名称、授课老师', value=course_name, enter=True)
        self.locator_view_select(id_value=course_name)
        self.locator_dialog_btn(btn_name='确定')
        # self.clear_then_input(self.course_teacher_plan_mould_search_input, course_name)
        # self.excute_js_click_ele(self.course_teacher_plan_mould_search_btn)
        # time.sleep(1)
        # self.excute_js_click_ele(self.checkbox)
        # time.sleep(0.75)
        # self.excute_js_click_ele(self.confirm_btn)

    @allure.title('导入课程')
    def import_courses(self, file):
        """
        教学计划编辑页->新增板块->新增课程模块->课程导入
        :param file: 导入课表文件路径
        """
        course_import_btn = (By.XPATH, '//*[@class="table-div-btns"]//*[contains(@class, "small")]//*[contains(text(), "课程导入")]')
        self.poll_click(course_import_btn)
        self.find_elms((By.CSS_SELECTOR, 'input[type=file]'))[-1].send_keys(file)
        time.sleep(1)
        self.locator_dialog_btn('确定')
        time.sleep(1)
        return self

    @allure.step("点击新增模块")
    def click_add_plan_module(self):
        """移动鼠标、点击新增模块并选择单元选项"""
        btn_module_add = (By.XPATH, '(//div[contains(@class,"teach_plan_module_top_bg")]//i[contains(@class,"add")])[1]')  # 增加
        btn_module_add_option = (By.XPATH, '(//div[@class="teach_plan_add_choose"]/ul/li[text()="单元"])[1]')  # 添加的选项
        time.sleep(1)
        self.mouse_hover_to_ele(self.module1)
        self.element_click(btn_module_add)
        self.element_click(btn_module_add_option)
        return self

    @allure.step("新增模块")
    def edit_teach_plan_module(self):
        input_title = (By.XPATH, '//div[contains(@class,"teach_plan_module_high")]//label[text()="标题："]/following-sibling::div/input')  # 标题
        input_sub_title = (By.XPATH, '//div[contains(@class,"teach_plan_module_high")]//label[text()="副标题："]/following-sibling::div/input')  # 副标题
        input_value = (By.XPATH, '//div[contains(@class,"teach_plan_module_high")]//label[text()="内容："]/following-sibling::div/textarea')  # 内容
        btn_save = (By.XPATH, '//div[contains(@class,"teach_plan_module_high")]//div[@class="teach_plan_edit_box_save green"]')  # 保存按钮
        dict_value = self.module_data()
        self.clear_and_input_enter(input_title, dict_value["title"])
        self.clear_and_input_enter(input_sub_title, dict_value["sub_title"])
        self.clear_and_input_enter(input_value, dict_value["value"])
        self.element_click(btn_save)
        time.sleep(1)
        return dict_value

    @allure.step("新增子模块")
    def edit_teach_plan_unit(self):
        input_unit_title = (By.XPATH, '//div[@class="teach_sub teach_plan_content"]//div[contains(@data-id,"virt_tree")]//label[text()="标题："]/following-sibling::div/input[@value=""]')  # 标题
        input_unit_sub_title = (By.XPATH, '//div[@class="teach_sub teach_plan_content"]//div[contains(@data-id,"virt_tree")]//label[text()="副标题："]/following-sibling::div/input[@value=""]')  # 副标题
        input_unit_value = (By.XPATH, '//div[@class="teach_sub teach_plan_content"]//div[contains(@data-id,"virt_tree")]//label[text()="内容："]/following-sibling::div/textarea')  # 内容
        btn_unit_save = (By.XPATH, '//div[@class="teach_sub teach_plan_content"]//div[contains(@data-id,"virt_tree")]//div[@class="teach_plan_edit_box_save green"]')  # 保存按钮
        dict_value = self.module_data()
        self.clear_and_input_enter(input_unit_title, dict_value["title"])
        self.clear_and_input_enter(input_unit_sub_title, dict_value["sub_title"])
        self.clear_and_input_enter(input_unit_value, dict_value["value"])
        self.element_click(btn_unit_save)
        time.sleep(1)
        return dict_value

    @allure.step("点击编辑模块")
    def click_edit_plan_module(self):
        """移动鼠标并点击编辑模块按钮"""
        btn_module_edit = (By.XPATH, '//div[contains(@class,"teach_plan_module_top_bg")]//i[contains(@class,"edit")]')  # 编辑
        self.mouse_hover_to_ele(self.module1)
        self.element_click(btn_module_edit)
        return self

    @allure.step("点击删除模块")
    def click_delete_plan_module(self):
        """移动鼠标并点击删除模块按钮"""
        btn_module_delete = (By.XPATH, '(//div[contains(@class,"teach_plan_module_top_bg")]//i[@class="layui-icon layui-icon-delete"])[1]')  # 删除
        self.mouse_hover_to_ele(self.module1)
        self.element_click(btn_module_delete)
        return self

    @allure.step("点击层级移动模块")
    def click_move_plan_module(self):
        """"移动鼠标并点击层级移动模块按钮"""
        self.mouse_hover_to_ele(self.module1)
        self.element_click(self.btn_module_move)
        return self

    @allure.step("点击上移模块")
    def click_move_up_plan_module(self):
        """移动鼠标并点击上移模块按钮"""
        btn_module_move_up = (By.XPATH, '//div[contains(@class,"teach_plan_module_top_bg")]//i[contains(@class,"up")]')  # 上移
        self.mouse_hover_to_ele(self.module1)
        self.element_click(btn_module_move_up)
        return self

    @allure.step("点击下移模块")
    def click_move_down_plan_module(self):
        """移动鼠标并点击下移模块按钮"""
        btn_module_move_down = (
            By.XPATH, '//div[contains(@class,"teach_plan_module_top_bg")]//i[contains(@class,"down")]')  # 下移
        self.mouse_hover_to_ele(self.module1)
        self.element_click(btn_module_move_down)
        return self

    @allure.step("点击层级移动模块")
    def click_move_plan_module(self):
        """移动鼠标并点击层级移动模块按钮"""
        self.mouse_hover_to_ele(self.module1)
        self.element_click(self.btn_module_move)
        return self

    @allure.step("点击版块")
    def click_module(self):
        self.element_click(self.module1)
        return self

    @staticmethod
    def module_data():
        """随机模块数据"""
        dict_value = {"title": randomTool.random_str(), "sub_title": randomTool.random_str(),
                      "value": randomTool.random_str()}
        return dict_value

    @allure.step("选择复制的教学计划")
    def choice_class_teach_plan(self, class_name="2021年春季学期市管干部进修二班"):
        search_teach_plan = (By.XPATH, '//input[@handler="search"]')  # 教学计划搜索框
        items_teach_plan = (By.XPATH, '//div[@class="datagrid_fixed datagrid_fixed_left"]//tr[@row_index="0"]//i')  # 列表项选项
        btn_teach_plan_yes = (By.XPATH, '//span[text()="确定"]//parent::a[@class="ds-button undefined"]')  # 确定按钮
        self.click_copy_teach_plan()
        self.wait_invisibility_ele(self.find_elem(self.loading))
        time.sleep(1)
        self.input_send_keys(search_teach_plan, class_name + Keys.ENTER)
        self.element_click(items_teach_plan)
        self.switch_to_frame_back()
        self.element_click(btn_teach_plan_yes)
        self.click_tip_yes()
        return self

    @allure.step("删除模块")
    def delete_module(self):
        self.click_delete_plan_module()
        self.click_tip_yes()
        ele = self.find_elem(self.loading)
        self.wait_invisibility_ele(ele)
        time.sleep(0.5)
        return self

    @allure.step("获取模块信息")
    def get_teach_plan(self):
        text_teach_plan = (By.XPATH, '//div[contains(@class,"module_top_bg")]/div[@class="teach_plan_title" or @class="teach_sub teach_plan_desc"]')  # 教学计划
        time.sleep(1)
        return self.trim_texts(self.driver.find_elements(*text_teach_plan))

    def get_teach_plan_title(self):
        text_teach_plan_title = (By.XPATH, '//div[contains(@class,"module_top_bg")]/div[@class="teach_plan_title"]/div[@class="teach_plan_title_info"]')  # 教学计划标题
        time.sleep(0.5)
        return self.trim_texts(self.driver.find_elements(*text_teach_plan_title))

    @allure.step("获取子模块信息")
    def get_teach_plan_module(self):
        text_teach_module = (By.XPATH, '//div[contains(@class,"teach_plan_module_high")]//div[@class="teach_plan_module"]')  # 教学计划模块
        return self.trim_texts(self.driver.find_elements(*text_teach_module))

    @allure.step("构造数据")
    def make_data2(self, res):
        str_ = res[-1]
        value = str_.split(")、")[-1]
        value = value.split("\n")
        return value

    @allure.step("获取教学计划详情信息")
    def get_teach_plan_detail(self):
        detail = (By.XPATH, '//div[@class="teach_plan_right_box"]')
        time.sleep(1)
        value = self.trim_text(detail)
        return value

    def goback_teach_plan_page(self):
        from djw.page.smart_school_sys.教务管理.教学管理.教学计划.teach_plan_page import TeachPlanPage
        self.close_current_browser()
        self.switch_to_handle()
        return TeachPlanPage(self.driver)

    @allure.step("获取目录内容")
    def get_content_value(self):
        text_content = (By.XPATH, '//div[@class="el-tree-node__content"]')  # 目录
        time.sleep(0.5)
        return self.trim_texts(self.driver.find_elements(*text_content))

    @property
    @allure.step('获取计划页右上方所有操作按钮文本')
    def right_btn_texts(self):
        right_btns = (By.CSS_SELECTOR, '.row-right')
        right_btns_eles = self.driver.find_element(*right_btns)
        return self.driver.execute_script('return arguments[0].textContent;', right_btns_eles)
