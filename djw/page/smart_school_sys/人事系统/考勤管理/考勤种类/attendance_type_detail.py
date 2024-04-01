from common.tools_packages import *


class AttendanceTypeDetail(BasePage):

    def edit_info(self, data: dict):
        if '名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['名称'])
        if '排序' in data:
            self.locator_text_input(ctrl_id='sort', value=data['排序'])
        if '考勤规则' in data:
            self.locator_select_list_value(ctrl_id='attend_rule', value=data['考勤规则'])
        if '需打卡星期' in data:
            self.locator_select_radio(ctrl_id='attend_weekdays', value=data['需打卡星期'])
        if '考勤部门' in data:
            self.locator_select_radio(ctrl_id='attend_scope', value='部门')
            self.locator_search_magnifier(ctrl_id='attend_depts')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=data['考勤部门'], enter=True)
            self.locator_tree_node_click(node_value=data['考勤部门'])
            self.locator_dialog_btn(btn_name='确定')
        if '考勤人员' in data:
            self.locator_select_radio(ctrl_id='attend_scope', value='人员')
            self.locator_search_magnifier(ctrl_id='attend_persons')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=data['考勤人员'], enter=True)
            self.locator_tree_node_click(node_value=data['考勤人员'])
            self.locator_dialog_btn(btn_name='确定')
        if '打卡地点' in data:
            for i in data['打卡地点']:
                self.locator_dialog_btn(btn_name='新增')
                self.locator_search_input(dialog_title='添加考勤地点', placeholder='请输入需要搜索的地名',
                                          value=i['地点'])
                self.locator_dialog_btn(btn_name='搜索')
                time.sleep(2)
                self.locator_text_input(ctrl_id='radius', value=i['半径'])
                self.locator_dialog_btn(btn_name='确定')
        time.sleep(2)
        self.locator_button(button_title='保存')
