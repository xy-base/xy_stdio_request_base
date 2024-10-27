# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "stdinput"
"""
  * @File    :   stdinput.py
  * @Time    :   2023/06/05 01:06:25
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""
import sys
import time


def printf(text):
    print(
        text,
        file=open(
            "./logs/out.log",
            "a+",
        ),
    )


def main():
    index = 0
    while True:
        index = index + 1
        if sys.stdin.readable():
            content = sys.stdin.readline()
            if content:
                printf(content)
        time.sleep(5)


if __name__ == "__main__":
    print("start")
    main()
