# -*- coding: UTF-8 -*-
__author__ = "yuyangit"
__doc__ = "client"
"""
  * @File    :   client.py
  * @Time    :   2023/06/04 23:14:10
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""

from pathlib import Path
import time
from xy_stdio_request_base.Base import Base
from xy_stdio_request_base.Task import ErrorTask, InputTask, OutputTask
from xy_string.utils import is_empty_string
from subprocess import Popen, PIPE
from datetime import datetime


def printf(text):
    print(
        text,
        file=open(
            "./logs/client.log",
            "a+",
        ),
    )


class ClientBase(Base):
    input_text = None
    output_text = None
    error_text = None
    filepath: Path | None = None
    process: Popen | None = None
    stdout_file = open("logs/output.log", "a+")
    stderr_file = open("logs/error.log", "a+")

    def create_process(self):
        if (
            isinstance(self.filepath, Path)
            and self.filepath.is_file()
            and self.filepath.exists()
            and self.filepath.suffix == ".py"
        ):
            self.process = Popen(
                f"python -u {self.filepath}",
                shell=True,
                stdin=PIPE,
                stdout=self.stdout_file,
                stderr=self.stderr_file,
                encoding="utf-8",
                universal_newlines=True,
            )
            if self.process:
                self.stdin = self.process.stdin # type: ignore
                self.stdout = self.stdout_file
                self.stderr = self.stderr_file
            else:
                self.stdin = None
                self.stdout = None
                self.stderr = None
        else:
            self.stderr = None
            self.stdout = None
            self.stderr = None

    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.create_process()
        self.write_input(f"start input from client {self.identifier}")
        self.write_output(f"start output from client {self.identifier}")
        self.write_error(f"start error from client {self.identifier}")

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
                f"client post {datetime.now().isoformat()} {title} => {text} {self.identifier}",
            )


def main():
    client = ClientBase(Path("./server.py"))
    client.start()
    while not client.closed:
        client.write_input(
            f"client input => {datetime.now().isoformat()} {client.identifier}"
        )
        client.write_output(
            f"client output => {datetime.now().isoformat()} {client.identifier}"
        )
        client.write_error(
            f"client error => {datetime.now().isoformat()} {client.identifier}"
        )
        print_sep = client.input_text or client.output_text or client.error_text
        if not is_empty_string(client.input_text):
            printf(
                f"{datetime.now().isoformat()} input_text => {client.input_text}",
            )
            client.input_text = None
        if not is_empty_string(client.output_text):
            printf(
                f"{datetime.now().isoformat()} output_text => {client.output_text}",
            )
            client.output_text = None
        if not is_empty_string(client.error_text):
            printf(
                f"{datetime.now().isoformat()} error_text => {client.error_text}",
            )
            client.error_text = None
        if print_sep:
            printf(
                "=========================================================================",
            )
        time.sleep(3)


if __name__ == "__main__":
    main()
