from common.tools_packages import *
from djw.page.smart_school_sys.后勤管理.场地管理.场地申请.site_apply import SiteApply


class SiteSummary(SiteApply):
    """场地统计"""

    @allure.step('检索场地申请统计')
    def search(self, activity_name: str = '', count: int = 1):
        """
        :param activity_name: 活动名称
        :param count: 检索预期条数
        """
        return super().search(activity_name, count)

    @allure.step('场地申请统计列表导出')
    def export(self, file_name='场地申请统计.xlsx'):
        return super().export(file_name=file_name)
