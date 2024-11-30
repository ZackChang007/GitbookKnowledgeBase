---
description: conda wiki
---

# conda

### conda env

```bash
# create env
conda create -n py310 python=3.10

# list envs
conda info -e

# del env
conda env remove -n py310

# 查看conda envs路径
conda config --show envs_dirs

# 修改conda envs的默认存储位置，后面创建的env会放置在默认位置
conda config --add envs_dirs <新路径>
conda config --add envs_dirs D:\conda_envs

# 移除conda envs原有的路径
conda config --remove envs_dirs <旧路径>

# 查看当前conda env的python.exe路径
# linux 
where python
# windows powershell
Get-Command python
where.exe python
```
