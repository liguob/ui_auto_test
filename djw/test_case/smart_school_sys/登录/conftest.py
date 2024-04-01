"""
============================
Author:杨德义
============================
"""
import pytest
from djw.page.smart_school_sys.登录.login_page import LoginPage


@pytest.fixture(scope='class')
def login_setup(create_driver):
    """
    PC登录前置方法
    返回PC登录页对象
    """
    driver = create_driver()
    pc_login_page = LoginPage(driver=driver)
    pc_login_page.driver.get(pc_login_page.host + pc_login_page.djw_main_url)
    yield pc_login_page
