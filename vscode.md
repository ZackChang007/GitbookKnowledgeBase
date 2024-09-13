# vscode
## jupyter中包导入路径设置
```python
from pathlib import Path
import os

# 显示当前Jupyter文件的路径
print(Path.cwd())
# 设置路径为project的根目录
project_root = "C:\\Users\\user\\repos\\repo_A\\"
os.chdir(project_root)
print(Path.cwd())

# 接下来即可正常导入repo_A的包
```
