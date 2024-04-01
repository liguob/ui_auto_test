"""
============================
Author:杨德义
============================
"""
import allure
import time
import random
from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_class_page import ArrangeClassPage
from selenium.webdriver.common.by import By
from collections import namedtuple
from common.decorators import change_reset_implicit

from typing import Literal
from selenium.webdriver.remote.webdriver import WebElement


class ArrangTestclassPage(ArrangeClassPage):
    """排课页"""

    # 左侧边栏活动 tab
    activity_tab = (By.CSS_SELECTOR, '#tab-activity')
    # 左侧边栏快捷排课 tab
    course_tab = (By.CSS_SELECTOR, '#tab-course')
    # 左侧边栏教学计划 tab
    plan_tab = (By.CSS_SELECTOR, '#tab-plan')

    # 左侧边栏关键字搜索输入框
    search_input = (By.CSS_SELECTOR, '.teas-schedule-box-search input')
    # 左侧边栏关键字搜索输入框右侧搜索按钮
    search_btn = (By.CSS_SELECTOR, '.teas-schedule-box-search .el-icon-search')

    # 快捷排课/教学计划/活动tab下所有可排内容
    draggable_items = (By.CSS_SELECTOR, '.teas-schedule-box-item-title-text')
    # 快捷排课/教学计划/活动tab下已展开教学形式分组下所有可排内容
    draggable_items_expand_group = (By.CSS_SELECTOR, '.teas-schedule-box-group[show] .teas-schedule-box-item-title-text')

    # 空白 (未排课) 排课单元格
    no_schedule_cell = (By.XPATH, '//*[@noschedule]//ancestor::*[@class="teas-schedule-table-body-warp"]')
    # 已排课单元格(已发布和未发布状态均可)
    schedule_cell = (By.XPATH, '//*[@class="teas-schedule-table-body-warp-course"]')

    # 已排课单元格悬浮新增按钮
    add_schedule_btn = (By.CSS_SELECTOR, '[class*=operation-box]:not([noschedule]) [type=add]')
    # 空白(未排课)排课单元格悬浮新增按钮
    no_schedule_add_btn = (By.CSS_SELECTOR, '[noschedule] [type=add]')

    # 已排课单元格(未发布状态下)/调课页 悬浮拖动按钮
    draw_schedule_btn = (By.CSS_SELECTOR, '[type=move]')
    # 已排课单元格(未发布状态下)/调课页 悬浮编辑按钮
    edit_schedule_btn = (By.CSS_SELECTOR, '[type=edit]')
    # 已排课单元格(未发布状态下)/调课页 悬浮备注按钮
    mark_schedule_btn = (By.CSS_SELECTOR, '[type=beizhu]')
    # 已排课单元格(未发布状态下)/调课页 悬浮分组按钮
    group_schedule_btn = (By.CSS_SELECTOR, '[type=group]')
    # 已排课单元格(未发布状态下)/调课页 悬浮删除按钮
    delete_schedule_btn = (By.CSS_SELECTOR, '[type=delete]')

    # 发布课表按钮
    publish_course_btn = (By.XPATH, '//*[@class="dsf-teas-many-schedule-head-bottom-right"]//*[not (contains(text(), "取消")) and contains(text(), "发布")]')
    # 取消发布(课表)按钮
    cancel_publish_course_btn = (By.XPATH, '//*[@class="dsf-teas-many-schedule-head-bottom-right"]//*[contains(text(), "取消发布")]')
    # 更新发布(课表)按钮
    update_publish_course_btn = (By.XPATH, '//*[@class="dsf-teas-many-schedule-head-bottom-right"]//*[contains(text(), "更新发布")]')

    # 新增排课组件内进入合班班次选择
    go_select_join_class = (By.CSS_SELECTOR, '[ctrl-id=organization] .ds-subtable-tools .ds-button[title*=选择]')
    # 新增排课组件内指定班次退出合班按钮
    quit_joined_class = (By.CSS_SELECTOR, '[ctrl-id=organization] .ds-subtable-button[title*=退出合班]')
    # 新增排课组件内解散合班按钮
    disband_join_classes = (By.CSS_SELECTOR, '[ctrl-id=organization] .ds-subtable-tools .ds-button[title*=解散合班]')

    # 合班弹框继续按钮
    combine_continue_btn = (By.XPATH, '//*[@class="el-dialog__title" and contains(text(), "合班")]//ancestor::*[@class="el-dialog__header"]//following-sibling::*[@class="el-dialog__footer"]//*[contains(text(), "继 续")]')
    # 冲突弹框继续按钮
    conflict_continue_btn = (By.XPATH, '//*[@class="el-dialog__title" and contains(text(), "冲突")]//ancestor::*[@class="el-dialog__header"]//following-sibling::*[@class="el-dialog__footer"]//*[contains(text(), "继 续")]')

    # 分组上课对象选择组件内未选项(小组/学员)
    available_group_item = (By.CSS_SELECTOR, '[role=group] .el-tree-node__label:not(.is_disabled)')

    # 某分组课所有分组单元格(传课程名)
    group_schedules = (By.XPATH, '//*[@type="name" and contains(text(), "{}")]//ancestor::*[@class="teas-schedule-table-body-warp-course" and @note="分组"]')

    # 某分组课任一分组悬浮删除按钮(传课程名)
    any_group_del_btn = (By.XPATH, '//*[@type="name" and contains(text(), "{}")]//ancestor::*[@class="teas-schedule-table-body-warp-course" and @note="分组"]//*[@type="delete"]')
    # 某分组课指定分组悬浮删除按钮(传课程名、分组编号)
    specific_group_del_btn = (By.XPATH, '//*[@type="name" and contains(text(), "{}({})")]//ancestor::*[@class="teas-schedule-table-body-warp-course" and @note="分组"]//*[@type="delete"]')
    # 分组课当前分组删除确认
    del_confirm_current_group = (By.XPATH,
     '//*[@class="el-dialog" and @aria-label="操作提示"]//*[contains(@class, "ds-button")]//*[contains(text(), "删除当前小组")]')
    # 分组课所有分组删除确认
    del_confirm_all_groups = (By.XPATH,
     '//*[@class="el-dialog" and @aria-label="操作提示"]//*[contains(@class, "ds-button")]//*[contains(text(), "删除所有小组")]')

    # 分组单元格
    grouped_schedule = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course-note-item[type=分组]')
    # 合班单元格
    joined_schedule = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course-note-item[type=合班]')
    # 冲突单元格
    conflict_schedule = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course-note-item[type=冲突]')

    # 分组标记
    grouped_mark = (By.CSS_SELECTOR, '//*[contains(@class, "course-note-item") and contains(text(), "分组")]')
    # 合班单元格标记
    joined_mark = (By.XPATH, '//*[contains(@class, "course-note-item") and contains(text(), "合班")]')
    # 冲突单元格标记
    conflict_mark = (By.XPATH, '//*[contains(@class, "course-note-item") and contains(text(), "冲突")]')

    # 排课新增/编辑弹框内放大镜加载按钮
    into_search_btn = (By.CSS_SELECTOR, '.el-input__suffix-inner')
    # 排课编辑弹框内课程、教室、教师内容框内清除小叉
    tag_close_fork = (By.CSS_SELECTOR, '.el-tag__close')
    # 排课新增/编辑弹框内时段/地点/授课老师修改按钮
    edit_inner_btn = (By.CSS_SELECTOR, '[title=修改]')

    # 课程搜索页内课程检索框、教师搜索页内教师检索框
    search_inner_input = (By.CSS_SELECTOR, '.search-input input')
    # 课程搜索页内课程检索按钮、教师搜索页内教师检索按钮
    search_inner_btn = (By.CSS_SELECTOR, '.search-button')
    # 课程搜索页内课程单选框、教师搜索页内教师勾选框
    checkbox = (By.CSS_SELECTOR, '[class*=is-scrolling] .el-checkbox__inner')

    # 课程搜索页内确定按钮、教师搜索页内确定按钮、教室选择页内确定按钮
    confirm_course_teacher_classroom_btn = (By.XPATH, '//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')
    # 删除已排课单元格内容确定按钮
    confirm_delete_schedule = (By.XPATH, '//*[@class="el-message-box__btns"]//*[contains(text(), "确定")]')
    # 排课新增/编辑弹框保存按钮
    save_btn = (By.CSS_SELECTOR, '.ds-button[title=保存]')
    # 排课时段时间控件确定按钮
    confirm_interval_time = (By.XPATH, '//*[@class="el-picker-panel__footer"]//*[contains(text(), "确定")]')

    @change_reset_implicit()
    @allure.step('合班或冲突判断并继续')
    def combine_conflict_accept(self):
        teacher_tip = self.find_elements_displayed((By.CSS_SELECTOR, '[aria-label="排课提醒"]'))
        if teacher_tip:
            continu_btn = (By.XPATH, '//*[contains(@class,"ds-button")]//*[contains(text(),"继续")]')
            self.element_click(continu_btn)
            # self.locator_dialog_btn(btn_name='继续')
        exist_combine = self.driver.find_elements(*self.combine_continue_btn)
        exist_conflict = self.driver.find_elements(*self.conflict_continue_btn)
        if exist_combine:
            self.excute_js_click_ele(exist_combine[0])
            conflict_continue_ele = self.driver.find_elements(*self.conflict_continue_btn)
            if conflict_continue_ele:
                self.excute_js_click_ele(conflict_continue_ele[0])
        if exist_conflict:
            self.excute_js_click_ele(exist_conflict[0])

        time.sleep(2)

    @change_reset_implicit()
    @allure.step('继续发布确认判断')
    def publish_trouble_confirm(self):
        confirm_publish_btn = (By.XPATH, '//*[text()="继续发布"]')
        exist_confirm_publish_btn = self.driver.find_elements(*confirm_publish_btn)
        if exist_confirm_publish_btn:
            self.poll_click(exist_confirm_publish_btn[0])
        notice = (By.XPATH, '//div[@class="el-dialog__title" and contains(text(),"短信")]')
        if self.judge_element_whether_existence(notice):
            self.locator_view_select_all(dialog_title="排课短信通知")
            self.locator_dialog_btn(btn_name="确定", dialog_title="排课短信通知")
            sure_btn = (By.XPATH, '//div[@class="el-message-box__btns"]//*[contains(text(),"确定")]')
            if self.judge_element_whether_existence(sure_btn):
                self.element_click(sure_btn)
                # self.locator_dialog_btn(btn_name='确定', dialog_title='提示')
                self.wait_success_tip()

    @allure.step('点击发布按钮')
    def publish_course(self):
        self.element_click(self.publish_course_btn)
        self.publish_trouble_confirm()
        # self.alert_tip(keyword='操作成功')
        return self

    @allure.step('点击取消发布按钮')
    def cancel_publish_course(self):
        self.element_click(self.cancel_publish_course_btn)
        self.alert_tip(keyword='操作成功')
        return self

    @allure.step('点击更新发布按钮')
    def update_publish_course(self):
        self.element_click(self.update_publish_course_btn)
        self.publish_trouble_confirm()
        self.alert_tip(keyword='操作成功')
        return self

    @allure.step('切至快捷排课tab')
    def switch_course_tab(self):
        self.excute_js_click_ele(self.course_tab)
        time.sleep(2)
        return self

    @allure.step('切至教学计划tab')
    def switch_plan_tab(self):
        self.excute_js_click_ele(self.plan_tab)
        time.sleep(2)
        return self

    @allure.step('切至活动tab')
    def switch_activity_tab(self):
        self.excute_js_click_ele(self.activity_tab)
        time.sleep(2)
        return self

    @allure.step('关键字搜索/快捷排课/教学计划/活动')
    def search(self, name):
        self.clear_then_input(self.search_input, name+'\n')
        # self.element_click(self.search_btn)
        time.sleep(1)
        return self

    @property
    @change_reset_implicit(2)
    @allure.step('获取快捷排课/教学计划/活动检索结果文本列表')
    def search_datas(self):
        item = (By.CSS_SELECTOR, '.teas-schedule-box-item-title-text-highlight')
        items = self.driver.find_elements(*item)
        return self.trim_texts(items)

    @allure.step('单选课程')
    def select_course(self, course_name):
        self.locator_search_input(placeholder='请输入课程名称', value=course_name, times=2, enter=True)
        self.locator_view_select(id_value=course_name, dialog_title='请选择')
        self.locator_dialog_btn(btn_name='确定')
        time.sleep(0.5)

    @allure.step('选择校区-教室')
    def select_classroom(self, campus_name: str, building_name: str, classroom_name: str):

        """
        :param campus_name: 校区名
        :param building_name: 楼宇名
        :param classroom_name: 教室名
        """
        if campus_name and building_name and classroom_name:
            into_search_classroom = (By.CSS_SELECTOR, '[ctrl-id=place] .el-input__suffix-inner')
            self.poll_click(into_search_classroom)
            # into_search_btns = self.driver.find_elements(*self.into_search_btn)
            # self.excute_js_click_ele(into_search_btns[3])
            time.sleep(0.5)
            # 校区选择
            campus_loc = (By.XPATH, f'//*[@class="ds-select-class-room-tabs"]//*[contains(@class, "el-tabs__item") and contains(text(), "{campus_name}")]')
            self.excute_js_click_ele(campus_loc)
            # 楼宇选择
            building_loc = (By.XPATH, f'//*[@class="ds-select-class-room-tree"]//*[contains(@class, "is-leaf")]//following-sibling::*[contains(text(), "{building_name}")]')
            self.excute_js_click_ele(building_loc)
            # 教室选择
            classroom_loc = (By.XPATH, f'//*[@class="ds-select-class-room-grid"]//*[contains(@class, "ds-select-class-room-item-box-name") and contains(text(), "{classroom_name}")]')
            self.excute_js_click_ele(classroom_loc)
            time.sleep(0.5)
            self.excute_js_click_ele(self.confirm_course_teacher_classroom_btn)
            time.sleep(0.5)

    @allure.step('选择教师')
    def select_teacher(self, teacher_name):
        if teacher_name:
            into_search_teacher = (By.CSS_SELECTOR, '[ctrl-id=constitutor] .el-input__suffix-inner')
            self.poll_click(into_search_teacher)
            # into_search_btns = self.driver.find_elements(*self.into_search_btn)
            # self.excute_js_click_ele(into_search_btns[4])
            time.sleep(1)
            self.clear_then_input(self.search_inner_input, teacher_name)
            self.excute_js_click_ele(self.search_inner_btn)
            time.sleep(1)
            self.excute_js_click_ele(self.checkbox)
            time.sleep(1)
            self.excute_js_click_ele(self.confirm_course_teacher_classroom_btn)
            time.sleep(0.5)

    @allure.step('首个空白排课单元格点+号进入排课')
    def into_arrang_for_course_evaluate(self):
        time.sleep(1)
        no_schedule_add_btns = self.driver.find_elements(*self.no_schedule_add_btn)
        self.excute_js_click_ele(no_schedule_add_btns[0])
        time.sleep(2.5)

    @allure.step('指定一个课程/教学计划/活动新增排课')
    def arrang_by_add(self, course_name: str,
                      campus_name: str = '', building_name: str = '', classroom_name: str = '',
                      teacher_name: str = ''
                      ):
        """
        :param course_name: 课程名
        :param campus_name: 校区名
        :param building_name: 楼宇名
        :param classroom_name: 教室名
        :param teacher_name: 教师名
        """
        self.into_arrang_for_course_evaluate()
        self.locator_search_magnifier(ctrl_id='item')
        self.select_course(course_name)
        self.select_classroom(campus_name, building_name, classroom_name)
        self.select_teacher(teacher_name)
        self.locator_button(button_title='保存')
        time.sleep(0.5)
        self.combine_conflict_accept()
        self.explicit_wait_ele_presence(self.schedule_cell, explicit_timeout=30)  # 等待排课内容保存进单元格
        self.explicit_wait_ele_lost(self.WEB_TIP)  # 等到保存提示消失
        return self

    @allure.step('随机选择快捷排课课程')
    def random_select_tree_course(self):
        # 随机选择未展开教学形式分组展开
        expand_group = (By.CSS_SELECTOR, '.teas-schedule-box-group:not([show]) .teas-schedule-box-group-title')
        expand_groups = self.driver.find_elements(*expand_group)
        self.poll_click(random.choice(expand_groups))
        # 随机确定已展开教学形式分组下可排内容
        drag_items = self.driver.find_elements(*self.draggable_items_expand_group)
        drag_item = random.choice(drag_items)
        # drag_items = self.driver.find_elements(*self.draggable_items)
        # drag_item = random.choice(drag_items)
        return drag_item

    @allure.step('随机一个课程/教学计划/活动拖拽排课')
    def arrang_drag_drop_random(self):
        drag_item = self.random_select_tree_course()
        # 随机确定空白(未排课)排课单元格
        no_schedule_cells = self.driver.find_elements(*self.no_schedule_cell)
        to_cell = random.choice(no_schedule_cells)
        # 拖拽排课至单元格
        self.drag_and_drop(drag_item, to_cell)
        # 合班/冲突判断并继续
        self.combine_conflict_accept()
        self.explicit_wait_ele_presence(self.schedule_cell, explicit_timeout=30)  # 等待排课内容保存进单元格
        return self

    @allure.step('随机一个课程/教学计划/活动拖拽排课至首个/末个可排单元格')
    def arrang_drag_drop_first_last(self, index: Literal[0, -1] = 0):
        drag_item = self.random_select_tree_course()
        no_schedule_cells = self.driver.find_elements(*self.no_schedule_cell)
        first_cell = no_schedule_cells[index]
        self.drag_and_drop(drag_item, first_cell)
        self.combine_conflict_accept()
        time.sleep(1)
        self.explicit_wait_ele_presence(self.schedule_cell, explicit_timeout=30)
        return self

    @allure.step('指定一个课程/教学计划/活动拖拽排课')
    def arrang_drag_drop_specific(self, name):
        self.clear_then_input(self.search_input, name+'\n')
        time.sleep(0.5)
        drag_items = self.driver.find_elements(*self.draggable_items_expand_group)
        drag_item = random.choice(drag_items)
        no_schedule_cells = self.driver.find_elements(*self.no_schedule_cell)
        to_cell = random.choice(no_schedule_cells)
        self.drag_and_drop(drag_item, to_cell)
        self.combine_conflict_accept()
        self.explicit_wait_ele_presence(self.schedule_cell, explicit_timeout=30)  # 等待排课内容保存进单元格
        return self

    @allure.step('选择合班班次并保存')
    def combine_class_save(self, class_name: str):
        self.poll_click(self.go_select_join_class)
        self.locator_search_input(placeholder='输入关键字进行过滤', value=class_name, times=2, enter=True)
        item = (By.XPATH, f'//*[contains(@class,"tree-node")]//*[contains(text(), "{class_name}")]')
        combine_class_item = self.explicit_wait_ele_presence(item, explicit_timeout=30)
        time.sleep(0.5)
        self.poll_click(combine_class_item)
        time.sleep(0.5)
        self.excute_js_click_ele((By.XPATH, '//*[text()="确定"]/..'))
        time.sleep(0.5)
        self.excute_js_click_ele(self.save_btn)

    @allure.step('合班班次列表:退出合班')
    def quit_combine_classes(self):
        self.poll_click(self.quit_joined_class)
        confirm_quit = (By.XPATH, '//*[@role="dialog" and @aria-label="提示"]//*[contains(text(), "确定")]')
        self.poll_click(confirm_quit)
        return self

    @change_reset_implicit(3)
    @allure.step('获取所有已排课单元格')
    def schedules(self):
        return self.driver.find_elements(*self.schedule_cell)

    @allure.step('随机一个已排单元格')
    def random_schedule(self):
        return random.choice(self.schedules())

    @property
    @allure.step('获取已排课单元格总数量')
    def schedules_count(self):
        return len(self.schedules())

    @allure.step('随机删除未发布状态下或调课页任一已排单元格中内容')
    def random_delete_one_schedule(self):
        self.click_random_selected_ele(self.delete_schedule_btn)
        self.excute_js_click_ele(self.confirm_delete_schedule)
        time.sleep(2)
        return self

    @change_reset_implicit()
    @allure.step('获取某一已排单元格的排课信息(时段、教学形式、课程名、授课教师、授课场地)具名元组')
    def schedule_info(self, schedule: WebElement = None, index: int = 0):
        interval_loc = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course-item[type=time]')
        teaching_form_loc = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course-item[type=type]')
        course_name_loc = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course-item[type=name]')
        teachers_loc = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course-item[type=ren]')
        classroom_loc = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course-item[type=address]')

        interval = self.driver.find_elements(*interval_loc)[index].text.strip()
        teaching_form = self.driver.find_elements(*teaching_form_loc)[index].text.strip()
        course_name = self.driver.find_elements(*course_name_loc)[index].text.strip()
        teachers = self.driver.find_elements(*teachers_loc)[index].text.strip()
        classroom = self.driver.find_elements(*classroom_loc)[index].text.strip()

        ScheduleInfo = namedtuple('ScheduleInfo', 'interval, teaching_form, course_name, teachers, classroom')
        return ScheduleInfo(interval, teaching_form, course_name, teachers, classroom)

    @change_reset_implicit(1)
    @allure.step('获取某分组课所有分组单元格显示课程名')
    def group_course_names(self, course_name: str) -> list:
        schedules_loc = (self.group_schedules[0], self.group_schedules[1].format(course_name))
        schedules = self.driver.find_elements(*schedules_loc)
        return [self.schedule_info(schedule, index).course_name for index, schedule in enumerate(schedules)]

    @allure.step('随机进入未发布状态下或调课页任一已排单元格编辑页')
    def go_random_edit_one_schedule(self):
        self.click_random_selected_ele(self.edit_schedule_btn)
        return self

    @allure.step('随机进入未发布状态下或调课页任一已排单元格分组页')
    def go_random_group_one_schedule(self):
        self.click_random_selected_ele(self.group_schedule_btn)
        return self

    @allure.step('打开分组开关')
    def on_group(self):
        yes_radio = (By.XPATH, '//*[@ctrl-id="shcedule_group"]//*[@class="el-radio__label" and contains(text(), "是")]')
        self.poll_click(yes_radio)
        return self

    @allure.step('关闭分组开关')
    def off_group(self):
        no_radio = (By.XPATH, '//*[@ctrl-id="shcedule_group"]//*[@class="el-radio__label" and contains(text(), "否")]')
        self.poll_click(no_radio)
        return self

    @allure.step('切换分组对象:小组/学员')
    def switch_group_type(self, by: Literal['小组', '学员']):
        by_radio = (By.XPATH, f'//*[@ctrl-id="group_type"]//*[@class="el-radio__label" and contains(text(), "{by}")]')
        self.poll_click(by_radio)
        return self

    @allure.step('点击自动分组')
    def auto_grouped(self):
        btn = (By.XPATH, '//*[@class="ds-subtable-tools"]//*[@class="head-right-item"]//*[contains(text(), "自动分组")]')
        self.poll_click(btn)
        time.sleep(1)
        self.save_group_settings()

        self.driver.implicitly_wait(time_to_wait=2)
        exist_conflict = self.driver.find_elements(*self.conflict_continue_btn)
        if exist_conflict:
            self.excute_js_click_ele(exist_conflict[0])
            time.sleep(3)
        return self

    @allure.step('分组设置表单保存')
    def save_group_settings(self):
        btn = (By.XPATH, '//*[@class="ds-page-foot"]//*[contains(text(), "保存")]')
        self.poll_click(btn)
        time.sleep(3)
        return self

    @property
    @change_reset_implicit(2)
    @allure.step('获取分组单元格数量')
    def grouped_cell_count(self):
        return len(self.driver.find_elements(*self.grouped_schedule))

    @change_reset_implicit(2)
    @allure.step('指定分组课程删除所有小组')
    def destroy_all_groups(self):
        group_del_btn = (By.XPATH, '//*[@class="teas-schedule-table-body-warp-course-note-item" and @type="分组"] //ancestor::*[@type="course"]//*[@type="delete"]')
        self.click_random_selected_ele(group_del_btn)
        self.poll_click(self.del_confirm_all_groups)
        time.sleep(2.5)
        return self

    @change_reset_implicit(2)
    @allure.step('指定分组课程删除当前小组')
    def destroy_single_group(self, course_name):
        self.click_random_selected_ele((self.any_group_del_btn[0], self.any_group_del_btn[1].format(course_name)))
        self.poll_click(self.del_confirm_current_group)
        return self

    @change_reset_implicit()
    @allure.step('选择上课地点组件判断清空已选地点')
    def judge_clear_selected_classrooms(self):
        selected_classroom_close_fork = (By.CSS_SELECTOR, '.ds-select-class-room-selected-tags .el-tag__close')
        selected_classroom_forks = self.driver.find_elements(*selected_classroom_close_fork)
        if selected_classroom_forks:
            for selected_classroom_fork in selected_classroom_forks:
                self.poll_click(selected_classroom_fork)
                time.sleep(0.25)

    @allure.step('调换教室')
    def transfer_classroom(self, campus_name, building_name, classroom_name):
        into_search_classroom = (By.CSS_SELECTOR, '[ctrl-id=place] .el-input__suffix-inner')  # 进入搜索教室放大镜按钮
        self.excute_js_click_ele(into_search_classroom)
        time.sleep(0.5)
        self.judge_clear_selected_classrooms()
        # 校区选择
        campus_loc = (By.XPATH, f'//*[@class="ds-select-class-room-tabs"]//*[contains(@class, "el-tabs__item") and contains(text(), "{campus_name}")]')
        self.excute_js_click_ele(campus_loc)
        # 楼宇选择
        building_loc = (By.XPATH, f'//*[@class="ds-select-class-room-tree"]//*[contains(@class, "is-leaf")]//following-sibling::*[contains(text(), "{building_name}")]')
        self.excute_js_click_ele(building_loc)
        # 教室选择
        classroom_loc = (By.XPATH, f'//*[@class="ds-select-class-room-grid"]//*[contains(@class, "ds-select-class-room-item-box-name") and contains(text(), "{classroom_name}")]')
        self.excute_js_click_ele(classroom_loc)
        self.excute_js_click_ele(self.confirm_course_teacher_classroom_btn)
        self.excute_js_click_ele(self.save_btn)
        self.combine_conflict_accept()
        time.sleep(1)
        return self

    @allure.title("点击更新发布")
    def update_release_and_judege_conflict(self):
        """点击更新发布，并判断是否有冲突，如果有冲突，点击继续发布"""
        self.locator_dialog_btn(btn_name="暂存")
        update_release = (By.XPATH, '//button//span[contains(text(),"更新发布")]')
        continue_release = (By.XPATH, '//*[contains(@class,"ds-button")]//*[contains(text(),"继续")]')
        if self.judge_element_whether_existence(update_release):
            self.element_click(update_release)
            if self.judge_element_whether_existence(continue_release):
                self.element_click(continue_release)
            message_notice = (By.XPATH, '//div[@class="el-dialog__title" and contains(text(),"短信")]')
            if self.judge_element_whether_existence(message_notice):
                self.locator_view_select_all(dialog_title="调课短信通知")
                self.locator_dialog_btn(btn_name="确定", dialog_title="调课短信通知")
            release_notice = (By.XPATH, '//*[@class="el-dialog__title" and contains(text(),"发布提醒")]')
            # tip = (By.XPATH, '//div[@class="el-message-box__title"]')
            sure_btn = (By.XPATH, '//div[@class="el-message-box__btns"]//*[contains(text(),"确定")]')
            if self.judge_element_whether_existence(sure_btn):
                self.excute_js_click_ele(sure_btn)
                # self.locator_dialog_btn(btn_name="确定", dialog_title="提示")
            # if self.judge_element_whether_existence(release_notice):
            #     if self.judge_element_whether_existence(
            #             loc=(By.XPATH, '//*[@role="dialog" and @aria-label="发布提醒"]//*[contains(text(),"继续发布")]')):
            #         self.locator_dialog_btn(btn_name="继续发布", dialog_title="发布提醒")

    @allure.step('判断清空已选教师')
    def judge_clear_selected_teachers(self):
        selected_teacher_close_fork = (By.CSS_SELECTOR, '[ctrl-id=constitutor] .el-tag__close')
        selected_teacher_forks = self.driver.find_elements(*selected_teacher_close_fork)
        if selected_teacher_forks:
            for selected_teacher_fork in selected_teacher_forks:
                self.poll_click(selected_teacher_fork)
                time.sleep(0.25)

    @allure.step('调换教师')
    def transfer_teacher(self, teacher_name):
        self.judge_clear_selected_teachers()
        into_search_teacher = (By.CSS_SELECTOR, '[ctrl-id=constitutor] .el-input__suffix-inner')  # 进入搜索教师放大镜按钮
        self.excute_js_click_ele(into_search_teacher)
        time.sleep(3.5)
        self.clear_then_input(self.search_inner_input, teacher_name)
        self.poll_click(self.search_inner_btn)
        time.sleep(1)
        self.poll_click(self.checkbox)
        time.sleep(0.5)
        self.excute_js_click_ele(self.confirm_course_teacher_classroom_btn)
        self.excute_js_click_ele(self.save_btn)
        self.combine_conflict_accept()
        time.sleep(1)
        return self

    @allure.step('调换上课时间')
    def transfer_interval(self, transfer_stime, transfer_etime):
        stime_loc = (By.CSS_SELECTOR, '[ctrl-id="min_start_datetime"] input')
        etime_loc = (By.CSS_SELECTOR, '[ctrl-id="max_end_datetime"] input')
        self.input_readonly_js(stime_loc, transfer_stime)
        self.input_readonly_js(etime_loc, transfer_etime)
        confirm_stime = (By.XPATH, '(//*[contains(@class, "is-plain")]//*[contains(text(), "确定")])[1]')
        confirm_etime = (By.XPATH, '(//*[contains(@class, "is-plain")]//*[contains(text(), "确定")])[2]')
        self.poll_click(confirm_stime)
        self.poll_click(confirm_etime)
        self.excute_js_click_ele(self.save_btn)
        self.combine_conflict_accept()
        time.sleep(1)
        return self

    @change_reset_implicit(2)
    @allure.step('多班排课')
    def arrang_multiple(self):
        classes = (By.CSS_SELECTOR, '.table-class-info-col-class-name')
        multiple_classes = self.driver.find_elements(*classes)
        # 单击激活每一班次并排入课程
        for multiple_class in multiple_classes:
            self.excute_js_click_ele(multiple_class)
            time.sleep(1)
            self.switch_course_tab().arrang_drag_drop_first_last(-1)
        time.sleep(1)
        return self
