# TOML
* Ref:
  * [Learn TOML in 10 Minutes (Tutorial)](https://www.youtube.com/watch?v=D_Jb52jw2HY)
* .toml文件示例:
```toml
# 注释, config.toml
name = "My Project"
version = "0.1.0"
website = "https://example.com"

[items]
numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c"]

# 上一级字典items，和子字典items.details嵌套
[items.details]
updated = true
author = "John Doe"
# 可读取识别日期格式
timestamp = 2021-01-01T12:34:56Z

[database]
# 字典database，嵌套子字典file
file.type = "sqlite"
file.path = "mydatabase.db"

[inline_table]
inline = {key = "value", number = 123}

# 数组table_group，每个元素是一个字典
[[table_group]]
fruit = "apple"

[[table_group]]
fruit = "banana"

[[table_group]]
fruit = "orange"
```
* 读取 TOML 文件:
```python
# 读取 TOML 文件
import tomllib  # python 3.11官方库
from pprint import pprint

def load_toml(path) -> dict:
    """load toml data from file"""

    with open(path, "rb") as f:
        toml_data: dict = tomllib.load(f)
        return toml_data

pprint(load_toml("./data/config.toml"), sort_dicts=False)


# 如果是python 3.9可用tomli
import tomli
from pprint import pprint

with open('./data/config.toml', 'rb') as f:
    data = tomli.load(f)

pprint(data, sort_dicts=False)
```
