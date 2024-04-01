# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
============================
# Time       ：2021/12/7 10:45
# Author     ：李国彬
============================
"""
import pytest


@pytest.fixture(scope='function')
def admin_go_edu_manage(djw_login_by_admin):
    """管理员进入教务管理"""
    return djw_login_by_admin().go_edu_manage_page()
