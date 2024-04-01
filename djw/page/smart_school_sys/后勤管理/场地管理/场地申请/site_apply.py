from common.tools_packages import *


class SiteApply(BasePage):
    """场地申请"""

    def chose_classroom(self, campus_name: str, building_name: str, classroom_name: str):
        """
        场地(教室)选取: 校区-楼宇-教室 -> 确定
        :param campus_name: 校区名
        :param building_name: 楼宇名
        :param classroom_name: 教室名
        """
        campus_loc = (By.XPATH, f'//*[@class="ds-select-class-room-tabs"]//*[contains(text(), "{campus_name}")]')
        building_loc = (By.XPATH, f'//*[@class="ds-select-class-room-tree"]//*[contains(text(), "{building_name}")]')
        classroom_loc = (By.XPATH, f'//*[@class="ds-select-class-room-grid"]//*[contains(text(), "{classroom_name}")]')
        confirm = (By.XPATH, '//*[@class="el-dialog__footer"]//*[contains(text(), "确定")]')
        self.poll_click(campus_loc)
        self.poll_click(building_loc)
        self.poll_click(classroom_loc)
        self.poll_click(confirm)

    @allure.step('填写场地申请单')
    def __edit_form(self, data: dict):
        if '活动名称' in data:
            self.locator_text_input(ctrl_id='name', value=data['活动名称'])
        if '使用时间' in data:
            sdate, edate = data['使用时间']
            script = """document.querySelector("[module-name='teas.logistics.site.edit']").__vue__.$vm.$viewData['teas_logistics_site.use'] = {sdate: arguments[0], edate: arguments[1]}"""
            self.driver.execute_script(script, sdate+' '+'00:00:00', edate+' '+'00:00:00')
        if '参与人数' in data:
            self.locator_text_input(ctrl_id='num', value=str(data['参与人数']))
        if '场地类型' in data:
            site_type_input = (By.CSS_SELECTOR, '[ctrl-id=type] input')
            self.poll_click(site_type_input)
            option = (By.XPATH, f'//*[@class="el-scrollbar"]//*[contains(text(),"教室")]')
            self.poll_click(option)
        if '申请场地' in data:
            magnifier = (By.XPATH, '//*[@class="ds-datachoice-input"]//*[contains(@class, "el-icon-search")]')
            self.poll_click(magnifier)
            campus, building, classroom = data['申请场地']
            self.chose_classroom(campus, building, classroom)
        if note := data.get('备注'):
            if note.strip():
                note_loc = (By.CSS_SELECTOR, '[ctrl-id=note] textarea')
                self.driver.find_element(*note_loc).send_keys(note)

    @allure.step('新增发送场地申请')
    def send_apply(self, data: dict, checker: str):
        """
        :param data: 申请信息
        :param checker: 审核人
        """
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self.__edit_form(data)
        self.locator_button(button_title='发送')
        self.process_send(checker=checker)
        sleep(3)
        self.switch_to_handle(index=-1)
        return self

    @allure.step('检索场地申请/场地申请统计')
    def search(self, activity_name: str = '', count: int = 1):
        """
        :param activity_name: 活动名称
        :param count: 检索预期条数
        """
        self.locator_search_input(placeholder='活动名称', value=activity_name)
        search_btn = (By.CSS_SELECTOR, '.head-right-item .search-button')
        self.poll_click(search_btn)
        self.wait_listDataCount_searched(count=count)
        return self

    @property
    @allure.step('获取审核状态')
    def check_status(self):
        status = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=status_text__value]')
        return self.trim_text(status)

    @allure.step('场地申请列表/场地申请统计列表导出')
    def export(self, file_name='场地申请.xlsx'):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name="导出", dialog_title="导出设置", need_close=True)
        return wait_file_down_and_clean(file_name=file_name)
