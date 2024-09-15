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
