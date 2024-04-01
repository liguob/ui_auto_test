from datetime import datetime, timedeltafrom typing import Literalfrom common.tools_packages import *from djw.page.smart_school_sys.宿管系统.room_system import RoomSystemfrom common.decorators import change_reset_implicitclass IndividualManage(RoomSystem):    """散客管理"""    # 房间列表房间盒子(房号+筛选房型、性别)    room_box = (By.XPATH,                '//*[@class="ds-dormitory-container"]//*[@title="{}"]//following-sibling::*[@class="inner"]//p[contains(text(), "{}")]//following-sibling::p[contains(text(), "{}")]//ancestor::*[@data-id]')    # 房间列表房间盒子(房号+筛选房型、性别) -< 用于房间分配页    room_box_inner = (By.XPATH,                      '//*[@class="ds-dormitory-container page-head-font-fixed"]//*[@title="{}"]//following-sibling::*[@class="inner"]//p[contains(text(), "{}")]//following-sibling::p[contains(text(), "{}")]//ancestor::*[@data-id]')    # 入住/预定表单姓名    person_name = (By.XPATH,                   '//*[@class="el-dialog__wrapper" and not(contains(@style, "display: none;"))]//*[@for="personName"]//following-sibling::*//input')    # 入住/预定表单身份证号    idcard = (By.XPATH,              '//*[@class="el-dialog__wrapper" and not(contains(@style, "display: none;"))]//*[@for="idCard"]//following-sibling::*//input')    # 入住/预定表单联系方式    mobile = (By.XPATH,              '//*[@class="el-dialog__wrapper" and not(contains(@style, "display: none;"))]//*[@for="phone"]//following-sibling::*//input')    # 散客按房间/按团体tab    room_team_tab = (By.XPATH, '//*[@class="ds-dormitory-left"]//*[@class="title"]//*[contains(text(), "{}")]')    # 散客入住/预定/续房/退房/换房按钮    action_btn = (By.XPATH,                  '//*[@class="el-dialog__wrapper" and not(contains(@style, "display: none;"))]//*[@class="list-box"]//li//span[contains(text(), "{}")]')    @allure.step('切至按房间')    def switch_tab_room(self):        by_room_loc = (By.XPATH, self.room_team_tab[1].format('按房间'))        self.poll_click(by_room_loc)        if self.find_elements_no_exception((By.XPATH, '//*[contains(text(),"确认同住")]')):            self.locator_dialog_btn(btn_name='确认同住')        return self    @allure.step('切至按团体')    def switch_tab_team(self):        by_team_loc = (By.XPATH, self.room_team_tab[1].format('按团体'))        self.poll_click(by_team_loc)        return self    @allure.step('按房间:树形图选中楼宇')    def select_tree_building(self, building_name: str):        self.expand_building_or_default_area(node_name=building_name)        return self    @allure.step('按房间:树形图选中楼层')    def select_tree_floor(self, building_name: str, floor_name: str):        """        :param building_name: 楼层所在楼宇名        :param floor_name: 楼层名        """        self.select_tree_building(building_name)        self.locator_tree_node_click(node_value=floor_name)        return self    def expand_building_or_default_area(self, node_name: str):        """        判断楼宇或默认分区是否已展开, 未展开时才点击, 已展开则不点击        :param node_name: 楼宇名或默认分区        """        node_loc = (By.XPATH, f'//*[@role="treeitem"]//*[contains(text(),"{node_name}")]/../..')        node = self.driver.find_element(*node_loc)        if 'is-expanded' not in self.get_ele_attribute(node, 'class'):            self.locator_tree_node_click(node_value=node_name)        return self    @allure.step('按房间:树形图选默认分区')    def select_tree_default_area(self, default_name='默认分区'):        self.expand_building_or_default_area(node_name=default_name)        return self    @allure.step('点击房间显示房间床位详情')    def chose_room(self, name):        name_click = (By.CSS_SELECTOR, f'[title="{name}"]')        self.element_click(name_click)        return self    @allure.step('输入单个散客信息')    def input_individual_info(self):        """return 散客姓名"""        username = randomTool.random_name_long()        self.clear_then_input(self.person_name, username)        self.clear_then_input(self.idcard, randomTool.random_idcard())        self.clear_then_input(self.mobile, randomTool.random_phone())        return username    @allure.step('散客预定/入住表单/续房/换房保存')    def save(self):        save_btn = (By.XPATH,                    '//*[@class="el-dialog__wrapper" and not(contains(@style, "display: none;"))]//*[@class="action-footer"]//*[contains(text(), "保 存")]')        self.poll_click(save_btn)        return self    @allure.step('确定关闭散客预定/入住概览浮窗')    def confirm(self):        confirm_btn = (By.XPATH,                       '//*[@class="el-dialog__wrapper" and not(contains(@style, "display: none;"))]//*[@class="dialog-footer"]//*[contains(text(), "确 定")]')        self.poll_click(confirm_btn)        return self    # @change_reset_implicit()    @allure.step('单个散客预定房间')    def booking_room(self):        booking_btn_loc = (self.action_btn[0], self.action_btn[1].format('预定'))        if booking_btns := self.driver.find_elements(*booking_btn_loc):            self.poll_click(booking_btns[0])            username = self.input_individual_info()            self.save()            return username    @change_reset_implicit()    @allure.step('单个散客取消预定房间')    def cancel_booking_room(self):        cancel_booking_btn_loc = (self.action_btn[0], self.action_btn[1].format('取消预定'))        if cancel_booking_btn := self.driver.find_elements(*cancel_booking_btn_loc):            self.poll_click(cancel_booking_btn[0])            return self    @change_reset_implicit()    @allure.step('单个散客入住房间')    def check_in_room(self):        clear_btn = (By.XPATH, '//button[@type="button"]/span[text()="已清理"]')        if self.judge_element_whether_existence(loc=clear_btn):            self.element_click(clear_btn)            sleep(0.5)        check_in_btn_loc = (self.action_btn[0], self.action_btn[1].format('入住'))        if check_in_btns := self.driver.find_elements(*check_in_btn_loc):            self.poll_click(check_in_btns[0])            username = self.input_individual_info()            self.save()            return username    @allure.step('单个散客续房')    def renewal_room(self, date: str) -> str:        """        :param date:%d 01-09 10-31        return 续房入住结束时间(时分转换至时分秒)        """        renewal_btn_loc = (self.action_btn[0], self.action_btn[1].format('续房'))        renewal_btn = self.driver.find_element(*renewal_btn_loc)        self.poll_click(renewal_btn)        renewal_etime_loc = (            By.XPATH, '//label[contains(text(), "续房入住时间")]//following-sibling::*//input[contains(@placeholder, "结束")]')        self.poll_click(renewal_etime_loc)        self.renewal_time_widget_control(date)        confirm = (By.XPATH, '//*[@class="el-picker-panel__footer"]//*[contains(text(), "确定")]')        self.poll_click(confirm)        renewal_etime = self.driver.execute_script('return arguments[0].value',                                                   self.driver.find_element(*renewal_etime_loc))        self.save()        return datetime.datetime.strptime(renewal_etime, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %H:%M:%S')    @change_reset_implicit()    @allure.step('续房修改时间')    def renewal_time_widget_control(self, date: str):        """        :param date: %d 01-09 10-31        """        store_date_loc = (By.XPATH,                          '//*[@x-placement]//*[contains(@class, "el-picker-panel__content") and contains(@class, "is-left")]//*[@class="el-date-table"]//*[contains(@class, "available")]//*[contains(text(), "{}")]')        store_date_loc = (store_date_loc[0], store_date_loc[1].format(date[1:])) if date.startswith('0') \            else (store_date_loc[0], store_date_loc[1].format(date))        store_date_ele = self.driver.find_element(*store_date_loc)        for _ in range(2):            self.excute_js_click_ele(store_date_ele)            time.sleep(0.25)    @allure.step('单个散客退房')    def check_out_room(self):        check_out_btn_loc = (self.action_btn[0], self.action_btn[1].format('退房'))        check_out_btn = self.driver.find_element(*check_out_btn_loc)        self.poll_click(check_out_btn)        confirm_check_out_btn = (By.XPATH, '//*[@class="el-message-box__btns"]//*[contains(text(), "确定")]')        self.poll_click(confirm_check_out_btn)        return self    @allure.step('单个散客换房')    def change_room(self, change_name, room_num: str,                    room_type: Literal['单间', '标间', '套房', '多人间'],                    room_sex: Literal['男性', '女性', '不限'] = '不限'                    ):        """       :param room_num 更新房间房号(唯一字段)       :param room_type 更新房间房型       :param room_sex 更新房间性别        """        change_btn_loc = (By.XPATH, '//p[contains(text(),"{}")]/parent::li//span[contains(text(), "换房")]'.format(change_name))        # change_btn_loc = (self.action_btn[0], self.action_btn[1].format('换房'))        # change_btn = self.driver.find_element(*change_btn_loc)        self.poll_click(change_btn_loc)        # 换房房间列表房间盒子(房号+筛选房型、性别)        to_room_loc = (By.XPATH,                       f'//*[@class="el-dialog__body"]//*[@title="{room_num}"]//following-sibling::*[@class="inner"]//p[contains(text(), "{room_type}")]//following-sibling::p[contains(text(), "{room_sex}")]//ancestor::*[@data-id]')        to_room = self.driver.find_element(*to_room_loc)        self.poll_click(to_room)        time.sleep(0.25)        self.save()        if self.find_elements_no_exception((By.XPATH, '//*[contains(text(),"确认同住")]')):            self.locator_dialog_btn(btn_name='确认同住')        return self    @allure.step('散客预定/入住默认时间控件修改')    def default_time_widget_control_booking(self, date: str):        """        date: %d 01-09 10-31        """        default_time_widget = (By.CSS_SELECTOR, '.sec-box input[placeholder*=开始]')        self.poll_click(default_time_widget)        # store_date_loc = (By.XPATH, '((//*[contains(@class, "in-range")]//preceding-sibling::*[contains(@class, "prev-month") and not(contains(@class, "disabled"))]//ancestor::tr//following-sibling::tr)[1]//td)[1]')        # store_date_loc = (By.CSS_SELECTOR, '.end-date+*')        # store_date_ele = self.driver.find_element(*store_date_loc)        store_date_loc = (By.XPATH,                          '//*[@x-placement]//*[contains(@class, "el-picker-panel__content")]//*[@class="el-date-table"]//*[contains(@class, "available")]//*[contains(text(), "{}")]')        store_date_loc = (store_date_loc[0], store_date_loc[1].format(date[1:])) if date.startswith('0') \            else (store_date_loc[0], store_date_loc[1].format(date))        store_date_ele = self.driver.find_element(*store_date_loc)        for _ in range(2):            self.excute_js_click_ele(store_date_ele)            time.sleep(0.25)        confirm = (By.XPATH, '//*[@class="el-picker-panel__footer"]//*[contains(text(), "确定")]')        time.sleep(0.5)        self.poll_click(confirm)        time.sleep(0.5)        return self    @allure.step('散客入住:过期房测试-默认时间控件修改')    def default_time_widget_control_expired(self):        default_time_widget = (By.CSS_SELECTOR, '.sec-box input[placeholder*=开始]')        self.poll_click(default_time_widget)        # 选择开始结束日期为当日        today_loc = (By.CSS_SELECTOR, '.today')        today_ele = self.driver.find_element(*today_loc)        for _ in range(2):            self.excute_js_click_ele(today_ele)            time.sleep(0.25)        time.sleep(0.5)        # 选择结束时间为此刻两分后        etime_loc = (By.CSS_SELECTOR, '[x-placement] input[placeholder*=结束时间]')        self.poll_click(etime_loc)        time.sleep(0.5)        hour, minute = self.next_two_minute_hm()  # 获取此刻两分后的时分(24小时制)元组        hour_ele_loc = (By.XPATH,                        f'(//*[@x-placement]//*[contains(@class, "el-time-panel") and @style=""]//*[contains(@class, "el-time-spinner__list")])[1]//li[contains(text(), "{hour}")]')        minute_ele_loc = (By.XPATH,                          f'(//*[@x-placement]//*[contains(@class, "el-time-panel") and @style=""]//*[contains(@class, "el-time-spinner__list")])[2]//li[contains(text(), "{minute}")]')        self.excute_js_click_ele(self.driver.find_element(*hour_ele_loc))        time.sleep(0.5)        self.excute_js_click_ele(self.driver.find_element(*minute_ele_loc))        time.sleep(0.5)        hour_minute_confirm = (By.CSS_SELECTOR, '[x-placement] .el-time-panel[style=""] .confirm')  # 时分滚动选择确定按钮        self.poll_click(hour_minute_confirm)        time.sleep(0.5)        # 确定        confirm = (By.XPATH, '//*[@class="el-picker-panel__footer"]//*[contains(text(), "确定")]')  # 整个控件确定按钮        self.poll_click(confirm)        time.sleep(0.5)        return self    @staticmethod    def next_two_minute_hm() -> tuple:        """此刻两分后的时分(24小时制)元组"""        next_minute_time = datetime.datetime.now() + timedelta(minutes=2)  # 此刻两分后的时间        hour, minute = next_minute_time.strftime('%H:%M').split(':')        return hour, minute    @allure.step('获取散客管理房间禁排文本显示')    def get_forbade_infos(self) -> int:        return self.get_ele_texts_visitable((By.CSS_SELECTOR, '.warning'))