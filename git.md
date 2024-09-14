## 把本地项目发布到github
```bash
# 在本地仓库文件夹下打开bash

# 查看之前设定的git config信息
git config --global --list --show-origin

# 如果是新机器，创建新的ssh公钥
# 参考：https://github.com/settings/keys
# 生成ssh公钥
ssh-keygen -t rsa -C '邮箱名 其他标识性字段'
# 查看公钥
cat /Users/admin/.ssh/id_rsa.pub
# 把公钥信息粘贴到github上

# 关于ssh
# 参考：https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys
# 查看所有ssh keys
ls -al ~/.ssh


# 在github建立一个和本地仓库同名的空repo，什么都不要创建，包括readMe、gitignore等

# 本地仓库文件初始化为git项目
git init

# 查看git项目状态
git status

# git add本地仓库文件
git add main.py
# 如果add全部文件，直接：
git add -A

# git commit到缓存空间
git commit -m "init commit"

# 查看log
git log

# 查看分支
git branch

# 第一次push的指令
git remote add origin https://github.com/ZackChang007/demo_repo.git
git branch -M main
```
## discard changes放弃更改
* 在一个git repo中，先把一个文件复制到别的地方，然后删除了该文件，再把这个文件复制回git repo，全程并没有修改文件，但是`git status`显示如下：`(use "git restore <file>..." to discard changes in working directory)`
```bash
# 这是因为当你将文件从Git repo中删除并再复制回来时，尽管文件内容没有改变，文件的元数据（如权限或时间戳）可能发生了变化。Git会检测到这些元数据的变化，并认为文件已经修改。

# 要解决这个问题，可以尝试以下几种方法：

# 检查文件的权限或时间戳： 有时复制操作可能改变文件权限或时间戳。你可以使用以下命令查看文件权限或时间戳的差异：
stat <filename>

# 忽略文件的权限变化： 如果你确定文件内容没有改变，但Git依然认为文件有所不同，可以忽略权限变化，运行以下命令：
git config core.fileMode false
# 这将告诉Git忽略文件权限的变化。

# 恢复文件到暂存区的状态： 如果你确定文件没有实际变化，可以使用 git restore 或 git checkout 来恢复文件：
git restore <filename>

# 或者：
git checkout -- <filename>

# 确认文件没有变化： 使用 git diff 查看文件的具体变化：
git diff <filename>
# 这样你可以更准确地判断问题所在。
```