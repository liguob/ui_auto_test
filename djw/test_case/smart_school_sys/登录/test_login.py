# encoding=utf-8
"""
============================
Author:杨德义
============================
"""
import time
import pytest
import allure
from pathlib import Path
from common.excel_tool import DjwPd

_data_path = Path(__file__).resolve(strict=True).parents[0]/'_data'


@pytest.mark.ydy
@allure.epic('杨德义')
@allure.feature("登录")
@allure.story("异常登录")
class TestLoginFail:

    @pytest.mark.parametrize('case', DjwPd.read_excel(str(_data_path/'test_login.xlsx'), 'login_fail'))
    def test_login_fail(self, case, login_setup):
        allure.dynamic.title(f"{case['title']}验证")
        data = eval(case['data'])
        lp = login_setup

        def clear_login_input():
            lp.clear_input(lp.login_name_input)
            lp.clear_input(lp.password_input)
            lp.clear_input(lp.code)
        clear_login_input()
        lp.login_fail(data['username'], data['password'], data['code'])
        time.sleep(0.25)
        fail_tip = lp.get_text_implicitly(lp.failTips)
        assert fail_tip == case['expect']


if __name__ == '__main__':
    pytest.main(['-s'])
