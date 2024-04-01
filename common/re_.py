"""
============================
Author:杨德义
============================
"""
import re


def _re(pattern, string):
    return re.search(pattern=pattern, string=string).group(1)


def _re_sub(pattern, repl, string):
    """调试中"""
    while re.search(pattern=pattern, string=string).group(1):
        string = string.replace(re.search(pattern=pattern, string=string).group(1), 'hello')
    return string
