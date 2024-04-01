from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage
from common.tools_packages import *


class MaterialManage(PersonnelSysPage):
    """人事系统-资料管理"""

    @allure.step('查询文件')
    def search_file(self, name):
        self.locator_search_input(placeholder='文件名', value=name, enter=True)
        return self

    @allure.step('上传文件')
    def upload_file(self, file):
        self.locator_tag_button(button_title='上传', file_path=file)
        self.wait_success_tip()
        return self

    @allure.step('删除文件')
    def del_file(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(2)  # 等待数据加载
        return self

    @allure.step('下载单个文件')
    def download_file(self, file_name: str):
        self.locator_view_button(button_title='下载', id_value=file_name.split('.')[0])
        return wait_file_down_and_clean(file_name=file_name)

    @allure.step('批量下载文件')
    def download_all_file(self):
        self.locator_button(button_title='下载')
        return wait_file_down_and_clean(file_name='人事资料.zip')
