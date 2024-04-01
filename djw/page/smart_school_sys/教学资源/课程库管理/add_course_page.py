import time
from common.excel_tool import ExcelToolsPandas
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.random_tool import randomTool
from djw.page.smart_school_sys.教学资源.课程库管理.course_manage_page import CourseManagePage
import random
from datetime import datetime

pd = ExcelToolsPandas()


class AddCoursePage(CourseManagePage):
    """新增课程页面"""
    # 基本信息
    frame = (By.XPATH, '//iframe[contains(@src,"/dsfa/teas/zygl/kck/views/editxzkc.html")]')  # 页面frame
    form_title = (By.XPATH, '//label[text()="基本信息"]')  # 表单标题
    # input_teach_form = (By.XPATH, '//label[text()="教学形式"]/following-sibling::div//input')  # 教学形式
    # input_course_type = (By.XPATH, '//div[@caption="kclb"]//input')  # 课程类别
    # input_near_teach_time = (By.XPATH, '//label[text()="最近授课时间"]/following-sibling::div//input')  # 最近授课时间
    # input_subject_type = (By.XPATH, '//label[text()="学科分类"]/following-sibling::div//input')  # 学科分类
    btn_teach_plan_upload = (By.XPATH, '//label[text()="相关教案"]/following-sibling::div//button')  # 教案上传
    # 授课教师
    sub_form_title = (By.XPATH, '//span[@class="sub_title"]//label[text()="授课教师"]')  # 副标题
    btn_clear_choice = (By.XPATH, '//div[@caption="lessonTeacher"]//a[text()="清空"]')  # 清空选择的教师
    # 师资选择
    input_choice_box_no = (By.XPATH, '//div/a[text()="取消"]')  # 选择弹窗的取消按钮
    btn_close = (By.XPATH, '//div[@caption="ButtonBar3"]//a[text()="关闭"]')  # 关闭

    input_course_name = (By.XPATH, '//*[@ctrl-id="name"]//input')  # 课程名称
    teach_form = (By.XPATH, '//div[@ctrl-id="teaching_form"]//input')  # 教学形式
    lesson_type = (By.XPATH, '//div[@ctrl-id="category"]//input')  # 课程类别
    near_teach_time = (By.XPATH, '//div[@ctrl-id="category"]//input')  # 最近授课时间
    subject_type = (By.XPATH, '//div[@ctrl-id="subject"]//input')  # 学科分类
    order_code = (By.XPATH, '//div[@ctrl-id="ds_order"]//input')  # 排序码
    course_intro = (By.XPATH, '//*[@ctrl-id="description"]//textarea')  # 课程简介

    @allure.step("获取页面、标签页标题")
    def get_course_page_title(self):
        text_title = (By.XPATH, '//label[@class="ds_label font_2"]')  # 页面标题
        self.wait_visibility_ele(text_title)
        title = self.trim_text(text_title)
        handle_title = self.driver.title
        return title, handle_title

    @allure.step("新增课程填写表单")
    def add_course(self, teacher=True, **kwargs):
        input_items = (By.XPATH, '//*[@ctrl-id="{}"]//input')
        course_intro = (By.XPATH, '//*[@ctrl-id="description"]//textarea')  # 课程简介
        value = {"course_name": randomTool.random_str(), "teach_form": '专题辅导', "lesson_type": '经济建设',
                 "near_teach_time": f'{datetime.now().strftime("%Y")}+年秋季', "subject_type": '政治', 'use_scope': '主体班',
                 'order_code': randomTool.random_num(), "course_intro": randomTool.random_str()}
        ctrl_id_list = {'course_name': 'name', 'teach_form': 'teaching_form', 'lesson_type': 'category',
                        'near_teach_time': 'lately_teach', 'subject_type': 'subject', 'order_code': 'ds_order'}
        value.update(kwargs)
        use_scope = (By.XPATH, '//*[@*="range"]//*[contains(text(),"{}")]/../*[1]'.format(value['use_scope']))  # 使用范围
        for i in 'course_name', 'order_code':
            if value[i]:
                self.clear_then_input((input_items[0], input_items[1].format(ctrl_id_list[i])), value[i])  # 随机输入课程名称
        self.clear_then_input(course_intro, value["course_intro"])  # 随机输入课程简介

        for i in ('teach_form', 'lesson_type'):
            if value[i]:
                self.chose_list_option(option_text=value[i])

        for i in ('subject_type',):
            self.locator_select_list_value(ctrl_id="subject", value="政治")
        if value['use_scope']:
            self.excute_js_click_ele(use_scope)
        if teacher:
            self.into_choice()  # 进入选择窗口
            from djw.test_base_cases.test_a_03_import_user import UserInfoFileName
            teacher_name = random.choice(pd.base_data_path(UserInfoFileName))['姓名']
            self.choice_teacher(teacher_name)  # 选择老师
            items = (By.XPATH, '//div[@ctrl-id="teacher"]//*[contains(@*,"is-scrolling")]//td[{}]')
            teach_items = list(map(lambda x: (items[0], items[1].format(x)), range(2, 6)))
            teach_info = self.publish_get_info(*teach_items, t=['teacher', 'sex', 'source', 'unit'])
            value['teacher_info'] = teach_info
        return value

    @allure.step("进入选择窗口")
    def into_choice(self):
        frame_choice_box = (By.XPATH, '//iframe[contains(@src,"dsfa/teas/zygl/szk/views/szxz.html")]')  # 师资弹窗的frame
        btn_choice_teacher = (By.XPATH, '//div[@ctrl-id="teacher"]//*[text()=" 选择 "]/..')  # 选择教师
        self.move_to_ele(btn_choice_teacher)
        self.excute_js_click_ele(btn_choice_teacher)
        # self.switch_to_frame_back()
        # self.switch_to_frame(frame_choice_box)
        return self

    @allure.step("搜索老师")
    def search_teacher(self, teacher_name):
        input_choice_box_search = (By.XPATH, '//*[@*="datagrid1"]//*[@*="search-input el-input"]/input')  # 选择弹窗的搜索框
        result = (By.XPATH, '(//label[text()="姓名"]/following-sibling::div)[1]/div[text()="{}"]'.format(teacher_name))
        self.clear_then_input(input_choice_box_search, teacher_name + Keys.ENTER)
        time.sleep(1)
        # self.wait_visibility_ele(result)
        return self

    @allure.step("选择老师")
    def choice_teacher(self, teacher_name):
        input_choice_box_yes = (By.XPATH, '//span[text()="确定"]/parent::a')  # 选择弹窗的确认按钮
        time.sleep(0.5)
        self.search_teacher(teacher_name)
        self.choice_option()
        self.excute_js_click_ele(input_choice_box_yes)
        return self

    def close_add_course(self):
        """关闭新增课程标签页"""
        from djw.page.smart_school_sys.教学资源.课程库管理.course_manage_page import CourseManagePage
        success_tip = (By.XPATH, '//p[@class="el-message__content"]')
        # self.wait_visibility_ele(success_tip)  # 等待保存成功的提示
        time.sleep(1)
        self.switch_to_handle()
        return CourseManagePage(self.driver)

    @allure.step("保存课程")
    def save_course(self):
        btn_save = (By.XPATH, '//div[@ctrl-id="section3"]//*[text()=" 保存 "]/..')  # 保存
        self.excute_js_click_ele(btn_save)  # 点击保存
        return self

    @allure.step("获取提示")
    def get_tip(self):
        fail_tip = (By.XPATH, '//*[@*="ds-error-text"]')
        return self.trim_text(fail_tip)

    @allure.step("新建课程")
    def add_course_and_choice_teach(self, teacher=True, **kwargs):
        """填写课程信息->进入师资选择->选择老师->保存课程"""
        course_info = self.add_course(teacher, **kwargs)
        self.save_course()
        self.switch_to_handle(index=-2)
        time.sleep(2)
        return course_info

    @allure.step("查看课程详情")
    def get_course_info_by_check(self):
        ctrl_id_list = ["name", "teaching_form", "category", "lately_teach", "subject", 'range', "description"]
        input_item = (By.XPATH, '//*[@ctrl-id="{}"]//span/span')
        order_code = (By.XPATH, '//div[@ctrl-id="ds_order"]//span')  # 排序码
        creater = (By.XPATH, '//*[@ctrl-id="ds_create_user_name"]/div')  # 创建人
        updater = (By.XPATH, '//*[@ctrl-id="ds_update_user_name"]/div')  # 修改人
        list_item = [(input_item[0], input_item[1].format(i)) for i in ctrl_id_list]
        for i in order_code, creater, updater:
            list_item.append(i)
        course_title = ('course_name', 'teach_form', 'lesson_type', 'near_teach_time', 'subject_type', 'use_scope',
                        'course_intro', 'order_code', 'creater', 'updater')
        course_info = self.publish_get_info(*list_item, t=course_title)[0]
        items = (By.XPATH, '//*[contains(@*,"is-scrolling")]//td[{}]')
        teach_items = list(map(lambda x: (items[0], items[1].format(x)), range(2, 6)))
        try:
            teach_info = self.publish_get_info(*teach_items, t=['teacher', 'sex', 'source', 'unit'])
        except Exception as e:
            teach_info = ['']
        course_info['teacher_info'] = teach_info
        return course_info
