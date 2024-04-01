import allure
import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from datetime import datetime
from common.decorators import change_reset_implicit
from common.random_tool import randomTool


def handle_month(month):
    """处理datetime.now().strftime('%m')为指定字符串格式"""
    if month.startswith('0'):
        month = month[1:]
    month += '月'
    return month


class SalaryManage(BasePage):
    now_time = datetime.now()
    now_year, now_month = now_time.strftime('%Y'), now_time.strftime('%m')
    default_data = {
                    '工资项目名称': randomTool.random_str(),
                    '工资类型': '在编人员工资',
                    '年份': now_year,
                    '工资月份': handle_month(now_month)
                   }

    @allure.step('选择年度')
    def select_year_tree(self, year: str = now_year):
        tree_year = (By.XPATH, f'//*[@role="treeitem"]//*[contains(text(),"{year}")]')
        self.poll_click(tree_year)
        time.sleep(0.25)
        self.wait_presence_list_data()
        return self

    def _edit_salary_project_info(self, data: dict):
        """编辑工资项目信息"""
        ... if not data else self.default_data.update(data)
        keys = self.default_data.keys()
        if '工资项目名称' in keys:
            self.locator_text_input(ctrl_id='name', value=self.default_data['工资项目名称'])
        if '工资类型' in keys:
            self.chose_list_option(option_text=self.default_data['工资类型'])
        if '年份' in keys:
            self.chose_list_option(option_text=self.default_data['年份'])
        if '工资月份' in keys:
            self.chose_list_option(option_text=self.default_data['工资月份'])
        self.locator_button(button_title='保存')
        return self.default_data['工资项目名称']

    @allure.step('新增工资项目')
    def add_salary_project(self, data=None):
        data = {} if not data else data
        self.locator_button(button_title='新增')
        return self._edit_salary_project_info(data)

    @allure.step('搜索工资项目')
    def search_salary_project(self, project_name):
        self.locator_tag_search_input(placeholder='项目名称', value=project_name)
        self.locator_tag_search_button()
        return self

    @allure.step('查看详情工资明细')
    def view_salary_detail(self, project_name):
        self.locator_view_button(button_title='详情', id_value=project_name)
        self.wait_open_new_browser_and_switch()
        return self

    @allure.step('检索工资明细列表')
    def search_salary_detail(self, username):
        self.locator_search_input(placeholder='姓名', value=username)
        self.locator_tag_search_button()
        return self

    @allure.step('指定工资项目人员工资导入')
    def import_salary(self, file):
        """
        :param file: 人员工资导入文件路径
        """
        time.sleep(1)
        input_ = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=导入]~input')
        self.driver.find_element(*input_).send_keys(file)
        time.sleep(2)
        self.locator_dialog_btn('确定')
        time.sleep(1)
        return self

    @allure.step('关闭工资导入浮页')
    def close_salary_import_frame(self):
        close_btn = (By.XPATH, '//*[@role="dialog"]//*[@class="el-dialog__footer"]//*[contains(text(), "关闭")]')
        self.excute_js_click_ele(close_btn)
        time.sleep(1)
