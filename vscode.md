# vscode
## jupyter中包导入路径设置
```python
"""方法一"""

from pathlib import Path
import os

# 显示当前Jupyter文件的路径
print(Path.cwd())
# 设置路径为project的根目录
project_root = "C:\\Users\\user\\repos\\repo_A\\"
os.chdir(project_root)
print(Path.cwd())

"""方法二"""

import sys
sys.path.append(r"C:\repos\repo_a")


# 接下来即可正常导入repo_A的包
```
