# -*- coding: UTF-8 -*-
__author__ = "yuyangit"
__doc__ = "ModuleData"
"""
  * @File    :   ModuleData.py
  * @Time    :   2023/06/03 10:36:13
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""

from importlib_resources import files
import xy_stdio_request_base


class ModuleData:
    def __init__(self):
        self.data_path = files(xy_stdio_request_base.__name__).joinpath("data")
