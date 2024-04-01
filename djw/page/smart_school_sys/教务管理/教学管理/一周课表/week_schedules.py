# encoding = utf-8
import typing
import random
from common.tools_packages import *
from djw.page.smart_school_sys.教务管理.教学管理.排课管理.arrang_testclass_page import ArrangTestclassPage


class WeekSchedules(ArrangTestclassPage):
    """一周课表"""

    # 时段字典信息(维护)
    # interval_dict = {'晨读': 5, '上午': 6, '下午': 7, '晚上': 8}
    # 左侧指定班次名超链接
    # class_name_loc = (By.CSS_SELECTOR, '.table-class-info-export[title*="{}"]')
    # 课表单元格
    # course_schedule = (By.XPATH, '//*[@class="teas-schedule-table-body-warp-course"]//*[@type="name" and @title!="" and contains(text(), "{}")]')
    # 周起止日期文本
    week_interval = (By.CSS_SELECTOR, '.teas-many-schedule-head-time-text')
    # 班次单元格
    classes_cell = (By.CSS_SELECTOR, '.table-left-class-info-col')

    @allure.step('切换主栏日期/主栏午别/主栏日期午别')
    def switch_display(self, display_mode: typing.Literal['主栏日期', '主栏午别','主栏日期午别']):
        expand_loc = (By.CSS_SELECTOR, '.dsf-teas-many-schedule-head-bottom-right .el-dropdown-selfdefine')
        option_loc = (By.XPATH, f'//*[@x-placement]//*[@class="el-dropdown-menu__item" and contains(text(), "{display_mode}")]')
        self.poll_click(expand_loc)
        time.sleep(0.5)
        self.poll_click(option_loc)
        time.sleep(0.5)
        return self

    @allure.step('检索指定某一班次')
    def search_class(self, class_name):
        class_search_input = (By.CSS_SELECTOR, '.el-input__inner[placeholder]')
        class_search_btn = (By.CSS_SELECTOR, '.el-icon-search')
        self.driver.find_element(*class_search_input).send_keys(class_name)
        self.poll_click(class_search_btn)
        self.wait_listDataCount_searched(tr=self.classes_cell, count=1)
        return self

    @property
    @allure.step('获取已排课程单元格元素')
    def arranged_course(self):
        course_loc = (By.CSS_SELECTOR, '.teas-schedule-table-body-warp-course')
        course = self.explicit_wait_ele_presence(course_loc)
        return course

    @property
    @allure.step('获取周起止日期文本')
    def week_interval_text(self):
        week_interval = self.explicit_wait_ele_presence(self.week_interval, explicit_timeout=30)
        return self.trim_text(week_interval)

    @property
    @allure.step('获取周课表导出文件全名')
    def week_schedule_filename(self):
        week_interval = self.week_interval_text
        return '至'.join([i.replace('-', '年', 1).replace('-', '月', 1) + '日' for i in
                week_interval.replace(' ', '').split('至')]) + '课表.xlsx'

    @allure.step('随机单班周课表导出')
    def export_one_class_schedules(self):
        classes_name = (By.CSS_SELECTOR, '.table-class-info-export')   # 左侧所有班次名超链接
        classes = self.explicit_wait_eles_presence(classes_name, explicit_timeout=15)  # 等待页面数据加载完成再导出
        self.poll_click(random.choice(classes))
        return wait_file_down_and_clean(self.week_schedule_filename)

    @allure.step('所有班周课表导出')
    def export_all_classes_schedules(self):
        # 所有班次周课表导出按钮
        export_all_btn = (By.XPATH, '//*[@class="dsf-teas-many-schedule-head-bottom"]//*[@type="button"]//*[contains(text(), "导出")]')
        self.explicit_wait_eles_presence(self.classes_cell, explicit_timeout=15)  # 等待页面数据加载完成再导出
        self.poll_click(export_all_btn)
        return wait_file_down_and_clean(self.week_schedule_filename)
