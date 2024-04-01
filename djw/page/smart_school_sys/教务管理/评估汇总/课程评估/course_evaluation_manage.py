import allure

from djw.page.smart_school_sys.主页.home_page import HomePage
from common.file_path import wait_file_down_and_clean


class CourseEvaluationSumPage(HomePage):
    """课程评价汇总"""

    @allure.step('查询班次')
    def search_class(self, name):
        self.locator_tag_search_input(placeholder='请输入班次名称', value=name)
        self.locator_tag_search_button()
        return self

    @allure.step('进入课程评价详情')
    def go_evaluate_info(self, name):
        self.locator_view_button(button_title='课程评价', id_value=name)
        self.wait_open_new_browser_and_switch()
        from djw.page.smart_school_sys.教务管理.评估汇总.课程评估.课程评价.course_evaluation_detail import CourseEvaluationDetail
        return CourseEvaluationDetail(self.driver)

    @allure.step('点击参评率统计')
    def click_evaluate_percent(self, name):
        self.locator_view_button(button_title='参评率统计', id_value=name)
        return self

    @allure.step('参评率统计学员查询')
    def search_stu(self, name):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name, dialog_title=' ')
        self.locator_tag_search_button(dialog_title=' ')
        return self

    @allure.step('课程评估班次信息导出')
    def download_class_info(self, file_name):
        self.locator_tag_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name=file_name)
