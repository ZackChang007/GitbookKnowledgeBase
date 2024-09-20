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


# 在github建立一个和本地仓库同名的空repo，什么都不要创建，
# 包括readMe、gitignore等；但可以添加项目描述

# 本地仓库文件初始化为git项目
git init

# 添加.gitignore文件, 内容取决于项目语言和内容，可咨询gpt生成
touch .gitignore

# 查看git项目状态
git status

# git add本地仓库文件
git add main.py
# 如果add全部文件，直接：
git add -A
git add .

# git commit到缓存空间
git commit -m "init commit"

# 查看log
git log

# 查看分支
git branch

# 第一次push的指令
git remote add origin https://github.com/ZackChang007/demo_repo.git
git branch -M main
git push -u origin main

git status
git pull
```
### Git 无法识别你的用户身份错误
* 在尝试提交代码时，Git 无法识别你的用户身份，即未设置`user.name`和`user.email`，导致 Git 无法记录提交者的信息。
* 解决办法：
```bash
# 方法一：设置全局的 user.name 和 user.email
# 如果你希望在所有的 Git 仓库中使用相同的姓名和邮箱，可以设置全局的 user.name 和 user.email：
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 方法二：仅为当前仓库设置 user.name 和 user.email
# 如果你希望只在当前项目中使用不同的身份信息，而不影响其他项目，可以为当前仓库单独设置：
git config user.name "Your Name"
git config user.email "your.email@example.com"

# 确认设置
# 设置完成后，你可以使用以下命令检查是否配置成功：
# 检查全局设置：
git config --global user.name
git config --global user.email

# 检查当前项目设置：
git config user.name
git config user.email
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
## Pull Request (PR)
### 员工A开发并提交代码
* 确认本地代码正常运行后，员工A创建一个新的分支，比如`tom_branch`，并将代码提交到这个分支。
```bash
git branch -a  # 查看所有分支（远程的和本地的），以及当前所在分支
git checkout master                    # 切换到主分支
git pull origin master                 # 确保主分支是最新的

# git checkout -b tom_branch  # 第一次使用，创建新的feature分支，参数-b表示创建并切换到一个新的分支
git checkout tom_branch  # 切换到tom_branch
git branch -a  # 查看所有分支（远程的和本地的），以及当前所在分支

"""切换到tom_branch后，再创建新的文件或修改已有文件，不要在master branch上变动和提交！！！"""

# 对实际无变化的文件执行git restore
git diff demo.py
git restore demo.py

git status
git add demo.py                    # 添加修改到暂存区
git status
git commit -m "Add feature X"  # 提交代码

git pull --rebase origin tom_branch   # 从远程分支拉取最新更新，并使用rebase方式合并
git push origin tom_branch   # 推送代码到远程分支
```
### 员工A创建Pull Request (PR)
* 员工A登录代码托管平台（如GitHub、GitLab或Bitbucket），并为`tom_branch`分支创建一个Pull Request（PR），将分支中的代码提交到主分支（main）。
* 在PR的描述中，员工A详细说明了所做的更改、功能实现和测试情况。
## 配置多个ssh公钥
* 编辑`~/.ssh/config`文件:
```config
# GitHub 个人账号配置
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly yes
  
# 公司 GitLab 账号配置
Host gitlab.com
    HostName gitlab.hmswork.space   
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```
* 然后，在`~/.ssh/config`文件中配置多个ssh公钥，每个公钥对应一个Host，并指定对应的私钥文件路径。
* **把GitLab仓库的远程地址由HTTPS方式改为SSH**：
  * 查看当前连接方式`git remote -v`, `https`开头的说明当前是https连接方式, `git@`开头的说明当前是ssh连接方式。
  * 改为SSH：
    * `git remote set-url origin git@gitlab.hmswork.space:repos/repo_name.git`
  * 改为HTTPS：
    * `git remote set-url origin https://gitlab.hmswork.space/repos/repo_name.git`
* 最后，在终端输入`ssh -T git@github.com`或`ssh -Tvvv git@gitlab.hmswork.space`，测试是否成功。
  * `-Tvvv`参数用于debug
  * 如果出现`Connection timed out`，可尝试`ping gitlab.hmswork.space`或者`curl -v telnet://gitlab.hmswork.space:22`
  * 有时候DNS解析可能有问题，可以尝试直接使用`ping`解析到的IP地址连接`ssh -Tvvv git@192.168.1.1`
