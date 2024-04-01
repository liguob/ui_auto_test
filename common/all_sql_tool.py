# -*- coding: utf-8 -*-

"""
============================
Author: 李国彬
Time:2021/5/7    13:38
============================
通用数据库连接处理
"""
import jaydebeapi
from common import *


class AllSqlTool:
    # 连接使用的driver配置
    jdbc_config_driver = {'mysql': 'com.mysql.cj.jdbc.Driver',
                          'dm': 'dm.jdbc.driver.DmDriver',
                          'st': 'com.oscar.BulkDriver',
                          'rdjc': 'com.kingbase8.Driver'}
    # 连接使用的jar配置
    jdbc_config_jar = {'mysql': 'mysql-connector-java-8.0.24.jar',
                       'dm': 'DmJdbcDriver18.jar',
                       'st': 'oscarJDBC16.jar',
                       'rdjc': 'kingbase8-8.2.0.jar'}

    def __init__(self):
        #  根据运行环境获取数据库的连接参数
        self.jdbc_driver = self.jdbc_config_driver[os.environ['env']]
        self.jdbc_jar = os.path.join(DRIVER_PATH, self.jdbc_config_jar[os.environ['env']])
        self.jdbc_url = os.environ['sql_url']
        self.jdbc_user = os.environ['sql_user']
        self.jdbc_pwd = os.environ['sql_pwd']
        # env_host = os.environ['host']
        # self.jdbc_url = conf(RUN_ENV[env_host]["db"], 'urlString')
        # self.jdbc_user = conf(RUN_ENV[env_host]["db"], 'userName')
        # self.jdbc_pwd = conf(RUN_ENV[env_host]["db"], 'passWord')
        # self.jdbc_jar = os.path.join(DRIVER_PATH, conf(RUN_ENV[env_host]["db"], 'jar'))

    def connect_db(self):
        """创建数据库连接"""
        conn = jaydebeapi.connect(self.jdbc_driver,
                                  self.jdbc_url,
                                  [self.jdbc_user, self.jdbc_pwd],
                                  self.jdbc_jar,
                                  )
        return conn

    @staticmethod
    def get_file_sql(file):
        # 读取sql文件内容
        with open(file, encoding="utf-8") as f:
            return f.read()

    def execute_edit_sql(self, sql_content: str):
        """执行数据库数据修改，更新的语句"""
        conn = self.connect_db()
        cursor = conn.cursor()
        # 关闭编译器中代码检测中有关检测 Exception 的选项
        # noinspection PyBroadException
        try:
            cursor.execute(sql_content)
        except Exception as e:
            pass
            # conn.rollback()
        cursor.close()
        conn.close()

    def execute_query_sql(self, sql_content: str):
        """执行数据库数据查询，返回查询结果"""
        conn = self.connect_db()
        cursor = conn.cursor()
        # 关闭编译器中代码检测中有关检测 Exception 的选项
        # noinspection PyBroadException
        try:
            cursor.execute(sql_content)
        except Exception as e:
            conn.rollback()
        row = [str(i[0]).lower() for i in cursor.description]  # 执行查询列名
        info = cursor.fetchall()
        result = [dict(zip(row, i)) for i in info]  # 将查询结果转换为字典格式
        cursor.close()
        conn.close()
        return result
