# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/3/22    11:09
============================
"""
from common.tools_packages import *

date_today = randomTool.random_now_time_calculate()  # 年-月-日格式的今天日期
date_today_behind2 = randomTool.random_now_time_calculate(time_format="%Y-%m-%d 00:00", days=2)  # 年-月-日格式的后天日期
date_today_behind3 = randomTool.random_now_time_calculate(days=3)  # 年-月-日格式的第三天日期


@allure.epic("李国彬")
@allure.feature("教务管理")
@allure.story("班次管理")
class TestClassManage:
    # 测试数据
    class_data_path = data_path("班次管理数据.xlsx")
    stu_data_path = data_path("学员管理数据.xlsx")
    stu_import_data = data_path("学员导入数据.xls")
    data_feature = DjwPd.read_excel(class_data_path, '未开始班次')[0]
    data_edit_class = DjwPd.read_excel(class_data_path, '修改班次信息')[0]
    data_add_student = DjwPd.read_excel_func(stu_data_path, '新增学员')[0]
    data_edit_student = DjwPd.read_excel(stu_data_path, '修改学员')[0]

    @allure.title("新增删除未开始班次信息")
    def test_add_feature_class_info(self, go_class_manage):
        data = self.data_feature.copy()  # 新增班次数据
        data["培训开始时间"], data["培训结束时间"] = date_today_behind3, date_today_behind3  # 培训时间（开始日期大于当前日期）
        data["网报开始时间"], data["网报结束时间"] = date_today_behind2, date_today_behind2  # 网报时间（结束日期小于等于报到结束日期）
        data["换人截止时间"] = date_today  # 换人截止时间
        current_time = str(int(time.time()))  # 时间戳
        add_name = data["班次名称"] = data["班次名称"] + '-' + current_time  # 班次名称（带时间戳）
        # 新增班次并删除班次
        step0 = go_class_manage.switch_feature_class().add_class(data).search_class(add_name).switch_feature_class()
        step0.del_class(add_name)
        # 获取班次数量
        num = step0.search_class(add_name).locator_view_num()
        assert 0 == num

    @allure.title("学员管理-新增学员-修改学员-删除学员")
    def test_edit_student(self, go_class_manage, future_class_name):
        class_name = future_class_name
        data_stu = self.data_add_student  # 新增学员数据
        edit_data = self.data_edit_student  # 修改学员数据
        stu_name = data_stu["姓名"]
        # 进入班次管理新增班次
        step0 = go_class_manage
        step0.switch_feature_class().search_class(class_name)
        # 新增学员、修改学员
        step1 = step0.go_student_manage(class_name).add_stu(data_stu).search_stu(stu_name).edit_stu(stu_name, edit_data)
        # 删除学员
        step1.locator_view_select(id_value=stu_name)
        num = step1.del_selected_stu().search_stu(stu_name).locator_view_num()
        assert num == 0

    @allure.title("导入-批量删除学员")
    def test_import_student(self, go_class_manage, future_class_name):
        # 进入班次管理,新增班次
        class_name = future_class_name
        search_key = '批量'  # 来源于导入学员数据的关键字
        step0 = go_class_manage.switch_feature_class().search_class(class_name)
        # 导入学员
        step1 = step0.go_student_manage(class_name)
        file = DjwPd.read_excel_func_save(self.stu_import_data)
        num = len(DjwPd.read_excel(file))
        step1.import_student(file)
        num0 = step1.search_stu(search_key).locator_view_num()
        assert num >= num0
        # 批量删除学员
        step1.locator_view_select_all()
        num1 = step1.del_selected_stu().search_stu(search_key).locator_view_num()
        assert num1 == 0
