## Linux
### 运维脚本
* 复制fromFolder的全部文件（包括子文件夹中的文件，但exclude指定文件）到toFolder的脚本
  - .sh脚本内容见下方
  - 将脚本保存为`copy_folder.sh`   
  - 赋予执行权限：`chmod +x copy_folder.sh`
  - 运行脚本：`./copy_folder.sh`
```copy_folder.sh
#!/bin/bash

# 定义文件夹路径
fromFolder="/home/user/test_folder/a"
toFolder="/home/user/test_folder/b"

# 定义需要排除的文件和文件夹列表
exclude_list=(
  ".gitignore"
  "aa/4.txt"
  "noCopy.txt"
  # 添加更多需要排除的文件或文件夹
)

# Step 1: 清空 toFolder 的全部内容
# rm -rf "${toFolder:?}/"*
find "$toFolder" -mindepth 1 -delete

# # Step 2: 复制文件（包括子文件夹），但排除指定文件
# rsync -av --exclude=".gitignore" "$fromFolder/" "$toFolder/"

# Step 2: 构造 rsync 排除选项
rsync_excludes=()
for exclude_item in "${exclude_list[@]}"; do
  rsync_excludes+=(--exclude="$exclude_item")
done

# Step 3: 复制文件（包括子文件夹），但排除指定文件
rsync -av "${rsync_excludes[@]}" "$fromFolder/" "$toFolder/"
```

* 切换不同版本的shell
```bash
# 查看所有shell版本
cat /etc/shells
# 查看系统环境变量中的默认shell版本
echo $SHELL
# 查看当前正在执行的shell版本
echo $0

# 切换到另外的shell
/usr/bin/tmux
# 查看当前正在执行的shell
echo $0
# 退出当前版本shell
exit
```
### vim
* 设定vi配置
```shell
# 切换到系统根目录
cd ~
vi .vimrc

# 写入以下内容并保存退出：
set nu  # 显示行号
syntax on  # 语法高亮
```
