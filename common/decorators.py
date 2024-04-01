"""
============================
Author:杨德义
============================
"""
from functools import update_wrapper
from typing import Union


def change_reset_implicit(implicit_timeout: Union[int, float] = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            """隐式等待时间临时重载"""
            arg = args[0]
            driver_ = getattr(arg, 'driver', None)
            driver_.implicitly_wait(implicit_timeout) if driver_ \
                else arg.implicitly_wait(implicit_timeout)
            try:
                value = func(*args, **kwargs)
            except Exception as exc:
                raise
            else:
                return value
            finally:
                driver_.implicitly_wait(arg.Default_Implicit_Timeout) if driver_ \
                    else arg.implicitly_wait(getattr(wrapper, 'basepage').Default_Implicit_Timeout)

        update_wrapper(wrapper, func)
        return wrapper

    return decorator
