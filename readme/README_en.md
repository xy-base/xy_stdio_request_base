# xy_stdio_request_base

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

Standard IO wrappers.

## Source Code Repositories

- <a href="https://github.com/xy-base/xy_stdio_request_base.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-opensource/xy_stdio_request_base.git" target="_blank">Gitee</a>  
- <a href="https://gitcode.com/xy-opensource/xy_stdio_request_base.git" target="_blank">GitCode</a>  

## Installation

```bash
# bash
pip install xy_stdio_request_base
```

## How to use

###### python script


```python
# main.py
import asyncio
from xy_stdio_request_base.Base import Base
from xy_string.utils import is_empty_string
from datetime import datetime

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

    def on_output(self, output_text: str):
        self.output_text = output_text
        self.print_text(
            "output",
            self.output_text,
        )
        return super().on_output(self.output_text)

    def on_input(self, input_text: str):
        self.input_text = input_text
        self.print_text(
            "input",
            self.input_text,
        )
        return super().on_input(self.input_text)

    def on_error(self, error_text: str):
        self.error_text = error_text
        self.print_text(
            "error",
            self.error_text,
        )
        return super().on_error(self.error_text)

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

```

```bash
# bash
python main.py
```

## License
xy_stdio_request_base is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  

## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```