from common.tools_packages import *
from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem


class ExpiredRoomsManage(RoomSystem):
    """过期房管理"""

    @allure.step('团体名称/姓名检索过期房记录')
    def search_expired_room(self, name: str):
        """
        :param name: 团体名称/姓名
        """
        self.locator_search_input(placeholder='团体名称/姓名', value=name, enter=True)
        return self

    @allure.step('轮询检索过期房')
    def poll_search_expired_room(self, name: str):
        """
        轮询检索过期房,续房后2分钟后才才可以刷到
        :param name: 团体名称/姓名
        """
        self.locator_search_input(placeholder='团体名称/姓名', value=name)
        search_btn = self.driver.find_element(*(By.CSS_SELECTOR, 'button.search-button'))
        self.poll_search(search_btn, explicit_timeout=120, poll_frequency=4)

    @allure.step('(过期房管理)续房')
    def expired_room_renewal(self, etime: str):
        """
        :param etime: 续房退房时间(%Y-%m-%d %H:%M)
        """
        renewal_btn = (
        By.XPATH, '//*[contains(@class, "is-scrolling")]//*[contains(@class, "small")]//*[contains(text(), "续房")]')
        self.poll_click(renewal_btn)
        self.locator_date(ctrl_id='renewal_enddatetime', value=etime)
        save_btn = (By.XPATH, '//*[@class="el-dialog__body"]//*[@slot-name="foot"]//*[contains(text(), "保存")]')
        self.poll_click(save_btn)
        return self

    @allure.step('(过期房管理)退房')
    def expired_check_out(self):
        check_out_btn = (
        By.XPATH, '//*[contains(@class, "is-scrolling")]//*[contains(@class, "small")]//*[contains(text(), "退房")]')
        self.poll_click(check_out_btn)
        return self
