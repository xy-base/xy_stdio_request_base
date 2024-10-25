# -*- coding: UTF-8 -*-
__author__ = "yuyangit"
__doc__ = "server"
"""
  * @File    :   server.py
  * @Time    :   2023/06/04 23:09:13
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""
import asyncio
from xy_stdio_request_base.Base import Base
from xy_string.utils import is_empty_string
from datetime import datetime
from xy_stdio_request_base.Task import ErrorTask, InputTask, OutputTask


def printf(text):
    print(
        text,
        file=open(
            "./logs/server.log",
            "a+",
        ),
    )


class ServerBase(Base):
    input_text = None
    output_text = None
    error_text = None

    # def on_output(self, output_text: str):
    #     self.output_text = output_text
    #     self.print_text(
    #         "output",
    #         self.output_text,
    #     )
    #     return super().on_output(self.output_text)

    # def on_input(self, input_text: str):
    #     self.input_text = input_text
    #     self.print_text(
    #         "input",
    #         self.input_text,
    #     )
    #     return super().on_input(self.input_text)

    # def on_error(self, error_text: str):
    #     self.error_text = error_text
    #     self.print_text(
    #         "error",
    #         self.error_text,
    #     )
    #     return super().on_error(self.error_text)

    def on_output(self, output_text: str, task: OutputTask):
        self.output_text = output_text
        self.print_text(
            "output",
            self.output_text,
        )
        return super().on_output(self.output_text, task)

    # def on_output(self, output_text: str):
    #     self.output_text = output_text
    #     self.print_text(
    #         "output",
    #         self.output_text,
    #     )
    #     return super().on_output(self.output_text, ) # type: ignore

    def on_input(self, input_text: str, task: InputTask):
        self.input_text = input_text
        self.print_text(
            "input",
            self.input_text,
        )
        return super().on_input(self.input_text, task)

    # def on_input(self, input_text: str):
    #     self.input_text = input_text
    #     self.print_text(
    #         "input",
    #         self.input_text,
    #     )
    #     return super().on_input(self.input_text)

    def on_error(self, error_text: str, task: ErrorTask):
        self.error_text = error_text
        self.print_text(
            "error",
            self.error_text,
        )
        return super().on_error(self.error_text, task)

    # def on_error(self, error_text: str):
    #     self.error_text = error_text
    #     self.print_text(
    #         "error",
    #         self.error_text,
    #     )
    #     return super().on_error(self.error_text)

    def print_text(self, title: str, text: str):
        if not is_empty_string(text):
            printf(
                f"server post {datetime.now().isoformat()} {title} => {text} {self.identifier}",
            )


async def main():
    server = ServerBase()
    server.start()

    while not server.closed:
        server.write_input(
            f"server input => {datetime.now().isoformat()} {server.identifier}"
        )
        server.write_output(
            f"server output => {datetime.now().isoformat()} {server.identifier}"
        )
        server.write_error(
            f"server error => {datetime.now().isoformat()} {server.identifier}"
        )
        print_sep = server.input_text or server.output_text or server.error_text
        if not is_empty_string(server.input_text):
            printf(
                f"{datetime.now().isoformat()} input_text => {server.input_text}",
            )
            server.input_text = None
        if not is_empty_string(server.output_text):
            printf(
                f"{datetime.now().isoformat()} output_text => {server.output_text}",
            )
            server.output_text = None
        if not is_empty_string(server.error_text):
            printf(
                f"{datetime.now().isoformat()} error_text => {server.error_text}",
            )
            server.error_text = None
        if print_sep:
            printf(
                "=========================================================================",
            )
        await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(main())
