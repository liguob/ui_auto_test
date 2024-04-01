# encoding=utf-8
"""
============================
Author:何凯
Time:2021/9/6 18:54
============================
"""
import allure
from djw.page.smart_school_sys.人事系统.personnel_system_page import PersonnelSysPage


class PositionMaintain(PersonnelSysPage):
    """岗位信息维护页面类"""

    def _edit_info(self, data: dict):
        keys = data.keys()
        if "岗位名称" in keys:
            self.locator_text_input(ctrl_id="name", value=data["岗位名称"])
        if "批次" in keys:
            self.locator_text_input(ctrl_id="batch", value=data["批次"])
        if "学历要求" in keys:
            self.locator_text_input(ctrl_id="degree_requirement", value=data["学历要求"])
        if "岗位编号" in keys:
            self.locator_text_input(ctrl_id="post_number", value=data["岗位编号"])
        if "招聘人数" in keys:
            self.locator_text_input(ctrl_id="figures", value=data["招聘人数"])
        if "岗位申报模板" in keys:
            self.chose_list_option(option_text="高端人才报名登记模板")
        if "岗位类型" in keys:
            self.chose_list_option(option_text="管理岗")
        if "开始时间" in keys and "结束时间" in keys:
            self.locator_date_range(ctrl_id="effective_date", start_date=data["开始时间"], end_date=data["结束时间"])
        if "专业代码" in keys:
            self.locator_text_input(ctrl_id="major_code", value=data["专业代码"])
        if "编制情况" in keys:
            self.locator_select_radio(ctrl_id="staffing", value=data["编制情况"])
        if "研究方向" in keys:
            self.locator_text_input(ctrl_id="content", tag_type="textarea", value=data["研究方向"])
        if "所属公告" in keys:
            self.locator_search_magnifier(ctrl_id='notice')
            self.locator_search_input(placeholder='请输入标题', value=data['所属公告'], enter=True)
            self.locator_view_select(id_value=data['所属公告'])
            self.locator_dialog_btn(btn_name='确定')
        if "招聘部门" in keys:
            self.locator_search_magnifier(ctrl_id='dept')
            self.locator_search_input(placeholder='输入关键字进行过滤', value=data['招聘部门'], enter=True)
            self.locator_tree_node_click(node_value=data['招聘部门'])
            self.locator_dialog_btn(btn_name='确定')
        # 非必填项
        if "备注" in keys:
            self.locator_text_input(ctrl_id="remark", tag_type="textarea", value=data["备注"])
        if "附件" in keys:
            self.locator_text_input(ctrl_id="annex", value=data["附件"], is_file=True)
        self.locator_button("保存")
        self.wait_success_tip()
        self.wait_browser_close_switch_latest()
        return self

    @allure.step('搜索岗位')
    def search_position(self, value=' '):
        self.locator_tag_search_input(placeholder='公告标题', value=value, enter=True, times=2)
        return self

    @allure.step("新增岗位信息维护")
    def add_position(self, data: dict):
        self.locator_tag_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self._edit_info(data)
        return self

    @allure.step("编辑岗位信息维护")
    def edit_position(self, notice, data: dict):
        self.locator_view_button(button_title="编辑", id_value=notice)
        self.wait_open_new_browser_and_switch()
        self._edit_info(data)
        return self

    @allure.step("发布岗位")
    def push_position(self, name):
        self.locator_view_button(button_title="发布", id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('取消发布岗位')
    def cancel_push_position(self, name):
        self.locator_view_button(button_title="取消发布", id_value=name)
        self.wait_success_tip()
        return self

    @allure.step('删除岗位')
    def del_position(self, name):
        self.locator_view_button(button_title="删除", id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        return self
