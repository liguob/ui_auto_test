import typing

from common.tools_packages import *
from djw.page.smart_school_sys.宿管系统.room_system import RoomSystem


class IndividualRecord(RoomSystem):
    """散客入住记录"""

    @allure.step('姓名检索散客入住记录')
    def search_username(self, username: str):
        """
        :param username: 散客姓名
        """
        self.locator_search_input(placeholder='姓名', value=username)
        self.locator_tag_search_button()
        return self

    @allure.step('入住时间范围检索散客入住记录')
    def search_range_date(self, sdate: str, edate: str):
        """
        :param sdate: 开始日期
        :param edate: 结束日期
        """
        sdate_loc = (By.CSS_SELECTOR, 'input[placeholder*=开始]')
        edate_loc = (By.CSS_SELECTOR, 'input[placeholder*=结束]')
        self.driver.find_element(*sdate_loc).send_keys(sdate)
        self.driver.find_element(*edate_loc).send_keys(edate)
        date_label = (By.CSS_SELECTOR, 'label[title=入住时间]')
        self.move_to_click(date_label)
        return self

    @property
    @allure.step('获取调房/续房/退房记录/过期房管理团体名称文本')
    def team_text(self):
        team_text_loc = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=team_text__value]')
        return self.trim_text(team_text_loc)

    @property
    @allure.step('获取散客入住记录退房日期/退房记录退房时间/过期房管理退房日期文本')
    def edate_text(self):
        edate_text_loc = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=edate__value]')
        return self.trim_text(edate_text_loc)

    @allure.step('散客入住记录获取换房原房退房日期和新房入住日期')
    def old_out_and_new_in_time(self, old_roomnum: str, new_roomnum: str) -> typing.Tuple[str, str]:
        """
        :param old_roomnum: 原房号(完整)
        :param new_roomnum: 新房号(完整)
        """
        locator = (By.XPATH, '//*[contains(@class, "is-scrolling")]//*[contains(@class, "roomnumber__value") and @title="{}"]//ancestor::tr//td//*[contains(@class, "{}")]')
        old_room_edate_loc = (locator[0], locator[1].format(old_roomnum, 'edate__value'))
        new_room_sdate_loc = (locator[0], locator[1].format(new_roomnum, 'sdate__value'))
        return self.trim_text(old_room_edate_loc), self.trim_text(new_room_sdate_loc)

    @property
    @allure.step('获取散客入住记录/退房记录/过期房管理房间号')
    def roomnums_text(self):
        roomnum_text_loc = (By.CSS_SELECTOR, '[class*=is-scrolling] [class*=roomnumber__value]')
        return self.trim_texts(self.driver.find_elements(*roomnum_text_loc))
