from selenium.webdriver.common.keys import Keys

from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.logistics_manage_page import LogisticsManagePage


class WeekMenuHandle(LogisticsManagePage):
    """一周菜单操作"""

    @allure.step('一周菜单表单填写')
    def __edit_form(self, data: dict):
        if '标题' in data:
            self.locator_text_input(ctrl_id='title', value=data['标题'])
        if note := data.get('备注'):
            if note.strip():
                note_loc = (By.CSS_SELECTOR, '[ctrl-id=remark] textarea')
                self.driver.find_element(*note_loc).send_keys(note)

    @allure.step('新增保存菜单')
    def save_menu(self, data: dict):
        self.locator_button(button_title='新增')
        self.__edit_form(data)
        self.locator_button(button_title='保存', dialog_title='一周菜单')
        return self

    @allure.step('新增发布菜单')
    def publish_menu(self, data: dict):
        self.locator_button(button_title='新增')
        self.__edit_form(data)
        self.locator_button(button_title='发布', dialog_title='一周菜单')
        return self

    @allure.step('一周菜单操作/查看列表检索')
    def search(self, menu_title, count: int = 1):
        """
        :param menu_title: 菜单标题
        :param count: 检索预期条数
        """
        self.locator_search_input(placeholder='请输入标题', value=menu_title+Keys.ENTER)
        self.wait_listDataCount_searched(count=count)
        return self

    @property
    @allure.step('获取状态')
    def status(self):
        status = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=release_status_text__value]')
        return self.trim_text(status)

    @allure.step('发布一周菜单')
    def menu_publish(self):
        btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=发布]')
        self.poll_click(btn)
        return self

    @allure.step('撤回一周菜单')
    def menu_unpublish(self):
        sleep(1)
        btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=撤回]')
        self.poll_click(btn)
        return self

    @allure.step('编辑一周菜单')
    def menu_edit(self, data: dict):
        btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=编辑]')
        self.poll_click(btn)
        self.__edit_form(data)
        self.locator_button(button_title='保存', dialog_title='一周菜单')
        return self

    @allure.step('删除一周菜单')
    def menu_delete(self):
        btn = (By.CSS_SELECTOR, '[class*=is-scrolling] .small[title=删除]')
        self.poll_click(btn)
        confirm = (By.XPATH, '//*[@class="el-message-box__btns"]//*[contains(text(), "确定")]')
        self.poll_click(confirm)
        return self
