from common.tools_packages import *
from djw.page.smart_school_sys.教学资源.edu_source_page import EduSourcePage


class VideoManege(EduSourcePage):

    def _edit_info(self, data: dict):
        if '课程名称' in data:
            self.locator_text_input(ctrl_id='title', value=data['课程名称'])
        if '视频文件' in data:
            self.locator_text_input(ctrl_id='video_file', is_file=True, value=data['视频文件'])
        if '课程类别' in data:
            self.locator_select_list_value(ctrl_id='category', value=data['课程类别'])
        if '讲课老师' in data:
            self.locator_search_magnifier(ctrl_id='teacher')
            self.locator_search_input(placeholder='姓名', value=data['讲课老师'], enter=True)
            self.locator_view_select(id_value=data['讲课老师'])
            self.locator_dialog_btn(btn_name='确定')
        if '观看范围' in data:
            self.locator_select_radio(ctrl_id='range', value=data['观看范围'])
        time.sleep(3)

    @allure.step('新增视频')
    def add_video(self, data: dict, action: str):
        self.locator_button(button_title='新增')
        self.wait_open_new_browser_and_switch()
        self._edit_info(data)
        with allure.step(action):
            self.locator_button(button_title=action)
        self.wait_browser_close_switch_latest()
        return self

    def change_push_status(self, name, action):
        """发布/取消发布"""
        with allure.step(action):
            self.locator_view_button(button_title=action, id_value=name)
            self.wait_success_tip()
            time.sleep(2)
        return self

    @allure.step('查询视频')
    def search_video(self, name):
        self.locator_search_input(placeholder='课程名称、授课老师', value=name, enter=True)
        return self

    @allure.step('删除视频')
    def del_video(self, name):
        self.locator_view_button(button_title='删除', id_value=name)
        self.locator_dialog_btn(btn_name='确定')
        self.wait_success_tip()
        time.sleep(2)
        return self

    @allure.step('导出视频库信息文件')
    def download_file(self):
        self.locator_button(button_title='导出')
        self.locator_dialog_btn(btn_name='导出', dialog_title='导出设置', need_close=True)
        return wait_file_down_and_clean(file_name='视频库.xlsx')

    @allure.step('查看视频详情')
    def view_detail(self, name):
        self.locator_view_button(button_title='查看', id_value=name)
        self.wait_open_new_browser_and_switch()
        time.sleep(2)
        name = self.get_ele_text_visitable((By.CSS_SELECTOR, '[ctrl-id="title"] [title]'))
        self.close_and_return_page()
        return name

    @allure.step('打开所有分享课程并查询课程')
    def into_search_share_video(self, name):
        self.locator_dialog_btn(btn_name='分享课程')
        time.sleep(2)
        self.excute_js_click((By.XPATH, '//*[@class="pc_url url_page"]//*[text()="打开"]'))
        self.wait_open_new_browser_and_switch()
        info = self.driver.current_url.split('/')
        url = f'{self.host}' + '/'.join(info[3:])
        self.driver.get(url)
        self.locator_search_input(placeholder='课程名称、授课老师', value=name, enter=True)
        return self.locator_view_num()

    @allure.step('进入单个课程分享详情')
    def into_share_video_detail(self, name):
        self.locator_view_button(button_title='分享', id_value=name)
        self.excute_js_click((By.XPATH, '//*[@class="pc_url url_page"]//*[text()="打开"]'))
        self.wait_open_new_browser_and_switch()
        info = self.driver.current_url.split('/')
        url = f'{self.host}' + '/'.join(info[3:])
        self.driver.get(url)
        # self.driver.get(self.host+'dsf5/page.html#/pc/teas/resource/video/unlimited')
        time.sleep(2)
        return self.get_ele_text_visitable((By.XPATH, f'//*[text()="{name}"]'))
