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

"""方法三"""

import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
while not os.path.exists(os.path.join(script_dir, ".gitignore")):
    script_dir = os.path.dirname(script_dir)
repo_path = script_dir
sys.path.append(repo_path)
# 接下来即可正常导入repo_A的包
```

## 为 Python 开发人员提供完整、实用的 VSCode 设置
* <https://www.youtube.com/watch?v=PwGKhvqJCQM>
