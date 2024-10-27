# xy_stdio_request_base

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 說明

標準輸入輸出封裝。

## 程式碼庫

- <a href="https://github.com/xy-base/xy_stdio_request_base.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-base/xy_stdio_request_base.git" target="_blank">Gitee位址</a>

## 安裝

```bash
# bash
pip install xy_stdio_request_base
```

## 使用

###### python腳本

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

## 許可證
xy_stdio_request_base 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```