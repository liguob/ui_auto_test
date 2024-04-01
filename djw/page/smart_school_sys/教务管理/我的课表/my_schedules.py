from common.tools_packages import *
from djw.page.smart_school_sys.教务管理.edu_manage_page import EduManagePage


class MySchedules(EduManagePage):
    """教务管理-我的课表页面类"""

    @allure.step('获取对应班次的课程名称')
    def get_arrange_course_name(self, class_name):
        name = (By.XPATH, f'//*[contains(text(), "{class_name}")]//'
                          f'ancestor::div[@class="schedule-course-box defautDay"]//*[@title]')
        return str(self.get_ele_text_visitable(name)).strip()

    @allure.step('批量上传课件')
    def upload_files(self, file):
        input_loc = (By.XPATH, '//*[contains(text(), "批量上传课件")]/../../input')
        self.find_elem(input_loc).send_keys(file)
        time.sleep(2)  # 等待文件上传
        return self

    @allure.step('单个上传课件')
    def upload_file(self, name, file):
        self.locator_view_button(button_title='上传课件', id_value=name, file=file)
        time.sleep(2)  # 等待文件上传
        return self

    @allure.step('点击课件数量进入详情')
    def click_view_files(self, name):
        self.excute_js_click((By.XPATH, f'//*[text()="{name}"]/ancestor::tr//*[@class="filesum"]'))
        time.sleep(2)  # 等待加载
        return self

    @allure.step('删除课件')
    def del_files(self):
        self.locator_view_select_all(dialog_title='课件详情')
        self.locator_button(button_title='删除')
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        self.locator_close_dialog_window()
        return self
