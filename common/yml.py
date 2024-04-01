# encoding=utf-8
"""
============================
Author:杨德义
============================
"""
import string

import yaml


def read_yaml(yaml_path):
    with open(yaml_path, mode='rb') as f:
        return yaml.safe_load(stream=f.read())


def read_yaml_api_parameter(yml_file, api_name, data: dict = None):
    """读取文件的yaml, 并初始化数据"""
    with open(yml_file, encoding='utf-8') as f:
        yml_str = yaml.safe_load(f)[api_name]
        # print(f'初始：{yml_str}')
        yml_str = yaml.safe_dump(yml_str)
        # print(f'yml进行dump:{yml_str}')
        yml_str_template = string.Template(yml_str)
        yml_str_data = yml_str_template.safe_substitute(data)
        # print(yml_str_data)
        yml_str_data = yaml.safe_load(yml_str_data)
        # print(f'替换后{yml_str_data}')
    return yml_str_data
