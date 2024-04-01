from common.tools_packages import *
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class PassportManage(PersonnelSysPage):
    """因私出国-证件管理页面类"""

    def _edit_info(self, data: dict):
        if '姓名' in data:
            self.locator_search_magnifier(ctrl_id='name')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=data['姓名'], enter=True)
            self.locator_tree_node_click(node_value=data['姓名'])
            self.locator_dialog_btn(btn_name='确定')
        if '到期时间' in data:
            self.locator_date(ctrl_id='expire_time', value=data['到期时间'])
        if '证件类型' in data:
            self.locator_select_list_value(ctrl_id='certificate_type', value=data['证件类型'])
        time.sleep(1)
        self.locator_button('保存')

    @allure.step('查询证件')
    def search_passport(self, name):
        self.locator_search_input(placeholder='请输入部门/姓名', value=name, times=2, enter=True)
        return self

    @allure.step('新增证件')
    def add_passport(self, data):
        self.locator_button(button_title='新增')
        self._edit_info(data)
        self.wait_success_tip()
        return self

    @allure.step('新增证件信息校验')
    def add_passport_check(self):
        self.locator_button(button_title='新增')
        self.locator_button('保存')
        return self.get_all_required_prompt()

    @allure.step('修改证件')
    def edit_passport(self, name, data):
        self.locator_view_button(button_title='修改', id_value=name)
        self._edit_info(data)
        self.wait_success_tip()
        time.sleep(1)  # 等待数据刷新
        return self

    @allure.step('删除证件')
    def del_passport(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self

    @allure.step('导出证件表')
    def download_passport(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='证件表.xlsx', times=20)
