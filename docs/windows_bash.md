# windows bash script
## 自动化运维
* 启动某个conda env，切换至目标文件夹，调用python intepreter运行.py文件
```bash
@echo off
echo Activating Conda environment...
call conda activate py310

echo Changing directory...
cd "C:\gh\repo_a\src"

echo Waiting for 3 seconds...
timeout /t 3 /nobreak

echo Running Python script...
python main.py

echo Script finished.
pause
```
