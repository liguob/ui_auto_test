from common.tools_packages import *
from common.decorators import change_reset_implicit
from djw.page.smart_school_sys.宿管系统.散客入住记录.individual_record import IndividualRecord


class ChangeRenewalRecord(IndividualRecord):
    """调房/续房记录"""
    # 换房记录检索表单行数
    change_tr = (By.XPATH, '//*[contains(@class, "is-scrolling")]//*[contains(@class, "type_text__value") and @title="换房"]//ancestor::tr')
    # 续房记录检索表单行数
    renewal_tr = (By.XPATH, '//*[contains(@class, "is-scrolling")]//*[contains(@class, "type_text__value") and @title="续房"]//ancestor::tr')

    @property
    @change_reset_implicit()
    @allure.step('获取换房记录检索展示条数')
    def table_count_searched_change(self):
        return len(self.driver.find_elements(*self.change_tr))

    @property
    @change_reset_implicit()
    @allure.step('获取续房记录检索展示条数')
    def table_count_searched_renewal(self):
        return len(self.driver.find_elements(*self.renewal_tr))
