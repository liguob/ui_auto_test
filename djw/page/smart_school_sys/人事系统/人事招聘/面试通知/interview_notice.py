# encoding=utf-8
from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class InterviewNotice(PersonnelSysPage):
    """面试通知页面类"""

    @allure.step('查询人员')
    def search_user(self, name):
        self.locator_tag_search_input(placeholder='请输入姓名', value=name, enter=True, times=2)
        return self

    @allure.step('下载准考证')
    def download_file(self):
        self.locator_view_select_all()
        self.locator_tag_button(button_title='下载准考证')
        return wait_file_down_and_clean(file_name='准考证')

    def operate(self, name, action):
        with allure.step(f'{action}'):
            self.locator_view_button(button_title=f'{action}', id_value=name)
            self.wait_success_tip()
        return self

    @allure.step('录入成绩')
    def record_score(self, name, score_data):
        self.locator_view_button(button_title='录入成绩', id_value=name)
        if '笔试成绩' in score_data:
            self.find_elem((By.CSS_SELECTOR, '[placeholder="请输入"]')).send_keys(score_data['笔试成绩'])
        if '面试成绩' in score_data:
            value = score_data['面试成绩']
            self.excute_js_click((By.CSS_SELECTOR, '[placeholder="请选择"]'))
            self.excute_js_click((By.XPATH, f'//li//span[contains(text(),"{value}")]'))
        self.locator_view_button(button_title='保存', id_value=name)
        return self

    @allure.step("录入对应人员成绩")
    def entry_grade(self, name, data: dict):
        self.locator_tag_search_input(placeholder="请输入姓名", value=name+Keys.ENTER)
        time.sleep(0.5)
        entry_grade_btn = (By.XPATH, '//*[contains(@class, "scrolling")]//*[contains(@class, "small") and @title="录入成绩"]')
        self.excute_js_click_ele(entry_grade_btn)
        sleep(0.5)
        keys = data.keys()
        if "面试结果" in keys:
            interview = (By.XPATH, '//div[contains(@class,"scrolling")]//div[@class="el-select"]')
            self.excute_js_click_ele(interview)
            time.sleep(0.5)
            if data["面试结果"] == "符合":
                conform = (By.XPATH, '//div[@x-placement]//*[contains(text(), "符合") and not(contains(text(), "不"))]/parent::li')
                self.excute_js_click_ele(conform)
            elif data["面试结果"] == "不符合":
                not_conform = (By.XPATH, '//div[@x-placement]//*[contains(text(), "不符合")]/parent::li')
                self.excute_js_click_ele(not_conform)
        if "笔试成绩" in keys:
            input_written = (By.XPATH, '//div[contains(@class,"scrolling")]//input[@placeholder="请输入"]')
            self.clear_and_input(input_written, data["笔试成绩"])
        self.locator_view_button(button_title="保存", id_value=name)
