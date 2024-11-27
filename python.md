## Tips and tricks
* datetime对象转化为str时的简写方式
```python
from datetime import datetime

# 以下两种写法返回值相同
f"{datetime.now():%X}"
f"{datetime.now():%H:%M:%S}"
``` 

* `all`是一个内置函数，用于检查可迭代对象（如列表、元组、集合等）中的所有元素是否都满足某个条件。如果所有元素都满足条件，all 函数返回 True；如果至少有一个元素不满足条件，`all`函数返回 False。
```python
form collections.ABC import Iterable

prices: Iterable[float] = [1.2, 3.4, 5.6, 7.8, 9.0]
if not all(isinstance(price, (int, float)) and price >=0 for price in prices):
    raise ValueError('All peices must be non-negative numbers')
```
### loguru配置
```python
# repo/utils/log.py

from loguru import logger
import os
import datetime


# 获取当前脚本文件的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))
# 持续向上查找目录，直到找到名为".gitignore"的文件
while not os.path.exists(os.path.join(script_dir, ".gitignore")):
    script_dir = os.path.dirname(script_dir)
# 将当前文件夹的路径设置为repo的根目录
repo_path = script_dir
log_dir = os.path.join(repo_path, "logs")
now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d-%H%M")
print(log_dir)
logger.add(os.path.join(log_dir, f"repo_{date_string}.log"))

```
