# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/6/1    15:30
============================
"""
import pytest

from common.file_path import data_path


@pytest.fixture(scope="function")
def go_class_manage(djw_login_by_admin):
    """进入教务管理页面"""
    return djw_login_by_admin().go_edu_manage_page().go_class_manage_page()