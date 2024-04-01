# encoding=utf-8
import os
import allure
import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from common.manage.manage_driver import ManageDriver

manage_func_driver = ManageDriver()  # func级别的driver
manage_class_driver = ManageDriver()  # class级别的driver


@pytest.fixture(scope="function")
def open_browser(request):
    def _open_browser(driver_type: str = 'web'):
        return manage_func_driver.append_driver(driver_type=driver_type)

    def close_driver():
        """关闭所有driver"""
        # 调试时可使用暂停，不关闭浏览器
        import time
        time.sleep(6000)
        manage_func_driver.close_drivers()

    request.addfinalizer(close_driver)
    return _open_browser


@pytest.fixture(scope='class')
def create_driver(request):
    """
    打开浏览器 创建driver
    used by ydy
    """

    def _open_browser(driver_type="web"):
        return manage_class_driver.append_driver(driver_type=driver_type)

    def close_driver():
        """关闭所有driver"""
        manage_class_driver.close_drivers()

    request.addfinalizer(close_driver)

    return _open_browser


@pytest.fixture(scope='class')
def create_mobile_driver(request):
    """
    打开浏览器 创建driver
    used by ydy
    """

    def _open_browser(driver_type="app"):
        return manage_class_driver.append_driver(driver_type=driver_type)

    def close_driver():
        """关闭所有driver"""
        # import time
        # time.sleep(6000)
        manage_class_driver.close_drivers()

    request.addfinalizer(close_driver)

    return _open_browser


def pytest_addoption(parser):
    """
    @author: liguobin、yangdeyi
    自定义命令行获取运行环境
    """
    # 控制UI自动化运行环境参数
    parser.addoption("--env",
                     action="store",
                     default="mysql",
                     help="which url(database) to run!",
                     )
    # 控制UI自动化运行是否无界面运行参数
    parser.addoption("--ui",
                     action="store",
                     default="t",
                     help="run testcase with ui")
    # 控制UI自动化是否使用selenium grid分布式运行
    parser.addoption("--grid",
                     action="store",
                     default="f",
                     help="run testcases by selenium grid")
    # 控制UI自动化运行的ip地址
    parser.addoption("--host",
                     action="store",
                     default='',
                     help="run testcases by host")
    # 数据库连接url
    parser.addoption("--sql_url",
                     action="store",
                     default='',
                     help="database connect url")
    # 数据库连接用户名
    parser.addoption("--sql_user",
                     action="store",
                     default='',
                     help="database connect user")
    # 数据库连接密码
    parser.addoption("--sql_pwd",
                     action="store",
                     default='',
                     help="database connect password")


@pytest.fixture(scope='session', autouse=True)
def set_env(request):
    """
    @author: liguobin、yangdeyi
    添加数据库命令行参数至环境变量中
    """
    os.environ["env"] = request.config.getoption("--env")
    os.environ["ui"] = request.config.getoption("--ui")
    os.environ["grid"] = request.config.getoption("--grid")
    os.environ["host"] = request.config.getoption("--host")
    os.environ['sql_url'] = request.config.getoption("--sql_url")
    os.environ['sql_user'] = request.config.getoption("--sql_user")
    os.environ['sql_pwd'] = request.config.getoption("--sql_pwd")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    skip_result = ['passed', 'skipped']
    report = outcome.get_result()
    if report.outcome not in skip_result:  # 通过或跳过的用例不执行截图
        all_drivers = manage_func_driver.drivers + manage_class_driver.drivers
        for driver in all_drivers:
            if isinstance(driver, WebDriver):
                try:
                    driver.switch_to.window(driver.window_handles[-1])
                    allure.attach(body=driver.get_screenshot_as_png(), name=f"用例失败浏览器末尾窗口截图",
                                  attachment_type=allure.attachment_type.PNG)
                except Exception:
                    print('driver无法连接，截图失败')

# def pytest_collection_modifyitems(items):
#     """搜集测试用例，并使基础测试用例先执行"""
#     # print('pytest 收集到的所有测试用例：\n', items)
#     new_items = items[:]
#     pre_items = []
#     # print('用例个数', len(new_items))
#     for item in new_items:
#         # print('---' * 10)
#         # print('用例名：', item.name)
#         # print('用例节点：', item.nodeid)
#         node_id = item.nodeid
#         if 'test_base_cases' not in node_id:
#             pre_items.append(item)
#             items.remove(item)
#     items.extend(pre_items)
#     # print('pytest 收集到的所有测试用例：\n', items)
