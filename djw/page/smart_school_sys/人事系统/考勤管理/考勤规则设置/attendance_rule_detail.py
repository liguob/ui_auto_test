from common.tools_packages import *


class AttendanceRuleDetail(BasePage):
    """考勤规则编辑页面"""

    def edit_info(self, data: dict):
        if '考勤规则名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['考勤规则名称'])
        if '排序' in data:
            self.locator_text_input(ctrl_id='sort', value=data['排序'])
        if '打卡类型' in data:
            self.locator_select_radio(ctrl_id='attend_type', value=data['打卡类型'])
            all_time_fields = [['work_on_time_morning', 'work_on_before_morning', 'work_on_after_morning'],
                               ['work_off_time_morning', 'work_off_before_morning', 'work_off_after_morning'],
                               ['work_on_time_afternoon', 'work_on_before_afternoon', 'work_on_after_afternoon'],
                               ['work_off_time_afternoon', 'work_off_before_afternoon', 'work_off_after_afternoon']]
            time_values = data['打卡时间']
            for i in range(len(time_values)):
                self.locator_date(ctrl_id=all_time_fields[i][0], value=time_values[i][0], confirm=True, need_clear=True)
                self.locator_text_input(ctrl_id=all_time_fields[i][1], value=time_values[i][1])
                self.locator_text_input(ctrl_id=all_time_fields[i][2], value=time_values[i][2])
        if '弹性打卡设置' in data:
            self.locator_select_radio(ctrl_id='elastic_attend_switch', value=data['弹性打卡设置'])
            if '上班最多可晚到' in data:
                radio_btn = (By.CSS_SELECTOR, '[ctrl-id=late_checkbox] .el-checkbox__input')
                self.excute_js_click(radio_btn)
                self.locator_text_input(ctrl_id='elastic_late', value=data['上班最多可晚到'])
            if '下班最多可早走' in data:
                radio_btn = (By.CSS_SELECTOR, '[ctrl-id=early_checkbox] .el-checkbox__input')
                self.excute_js_click(radio_btn)
                self.locator_text_input(ctrl_id='elastic_early', value=data['下班最多可早走'])
        time.sleep(2)
        return self.locator_button(button_title='保存')
