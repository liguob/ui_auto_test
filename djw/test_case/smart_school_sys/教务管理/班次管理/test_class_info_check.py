# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/4/27    14:40
============================
"""
from common.tools_packages import *


@allure.epic("李国彬")
@allure.feature("教务管理")
@allure.story("班次管理")
class TestClassInfoCheck:

    @allure.title("班次信息必填校验")
    def test_class_info_check(self, go_class_manage):
        result = go_class_manage.add_class_fail({})
        assert result == ['该项必须填写', '该项必须填写', '该项必须填写', '该项必须填写', '该项必须填写']
