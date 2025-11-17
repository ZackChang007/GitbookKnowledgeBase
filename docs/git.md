# git

## 把本地项目发布到github

```bash
# 在本地仓库文件夹下打开bash

# 查看之前设定的git config信息
git config --global --list --show-origin

# 如果是新机器，创建新的ssh公钥
# 参考：https://github.com/settings/keys
# 生成ssh公钥
ssh-keygen -t rsa -C '邮箱名 其他标识性字段'
ssh-keygen -t ed25519 -C "your_email@example.com"
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

### 个人git管理整个repo_A，公司gitlab管理repo_A下的子目录repo_AA

* ssh config文件已经配置了github和gitlab的ssh key 

```bash
cd repo_A/repo_AA
# 初始化子仓库
git init --initial-branch=main


# 设置 Git 用户名（仅作用于当前仓库）
git config user.name "Your Company Name"
# 设置 Git 邮箱（建议与你的 GitLab 公司账户一致）
git config user.email "you@company.com"

# 这会在 repo_AA/.git/config 中添加类似：
[user]
    name = Your Company Name
    email = you@company.com

# 查看当前生效的配置
git config user.name
git config user.email


git remote add origin git@gitlab.hmswork.space:your_gitlab_user/repo_AA.git
cat .git/config

git add test.txt
git commit -m "add test.txt"
# 将本地分支 main 与远程的 origin/main 关联起来（建立 upstream tracking 关系）
# 只有初次commit时才需要执行，以后直接git push即可
git push --set-upstream origin main
# 或者以下也和上面命令相同
git push -u origin main


#########################日常开发方式###########################
# 在个人github repo_A上进行日常开发和git维护
# 每次有commit，先向github repo_A提交
# 然后切换到gitlab repo_AA，把相关修改和commit msg提交到gitlab
```

## 切换到某次历史的 commit 提交

```bash
# 查找目标 commit 的哈希值，显示你所有的 commit，找到你要切换的 commit 哈希值（前几位即可）。
git log

# 切换到该 commit，此时你处于“分离 HEAD”状态，意味着没有在任何分支上，而只是查看某个历史状态。
git checkout <commit-hash>
# 例如：
git checkout 1a2b3c4d

# 如果需要返回到最新的 commit 或继续开发：
git checkout <branch-name>
git checkout main
```

## .ipynb换行符格式不一致

* `warning: in the working copy of 'demo.ipynb', LF will be replaced by CRLF the next time Git touches it`
  * 在 Windows 系统上，换行符通常是 `CRLF`（回车+换行），而在 Linux 和 macOS 上，换行符通常是 `LF`（换行）。Git 在跨平台协作时，会自动处理这些换行符，但在某些情况下可能会给出这个警告，表示它将在下次修改文件时将换行符从 `LF` 转换为 `CRLF`。
* 解决方法：添加`.gitattributes`文件
  * 在项目根目录下添加一个`.gitattributes`文件，明确指定哪些文件使用哪种换行符。例如，针对 `.ipynb` 文件，可以指定使用`LF`：`*.ipynb text eol=lf`
  * `.gitattributes`的全局影响可能影响除了`.ipynb`文件之外的其他类型文件，如`.md`文件；如果不希望影响其他文件，可以在`.gitattributes`中明确指定不同文件类型的规则，如：`*.md text=auto`
  * `git add .gitattributes`
  * 规范化文件的换行符：`git add --renormalize .`
  * 提交更改：`git commit -m "Apply .gitattributes and normalize line endings"`

## PAT(Personal Access Token)

* GitHub——Settings——Developer settings——Personal access tokens > Tokens (classic) > Generate new token

```bash
# 直接在命令中使用PAT，有安全隐患，会被记录在bash_history中
git clone https://<PAT>@github.com/your_username/repo.git
# 查看最近5条bash history
history 5
# 删除bash history
history -c  # 清除当前会话的历史记录。
history -w  # 将当前清空的历史记录立即写入 .bash_history 文件，覆盖之前的记录。

# PAT设置在环境变量中，并在使用后删除
export GITHUB_TOKEN="your_personal_access_token_here"
git clone https://$GITHUB_TOKEN@github.com/your_username/your_repo.git
unset GITHUB_TOKEN  # 清除环境变量

# 使用临时变量（无记录）
GITHUB_TOKEN="your_token" git clone https://$GITHUB_TOKEN@github.com/your_username/your_repo.git

# 使用 read 读取 Token
read -s -p "Enter your GitHub PAT: " GITHUB_TOKEN  # -s 选项将隐藏输入
git clone https://$GITHUB_TOKEN@github.com/your_username/your_repo.git

# 在 .env 文件中管理
# 您可以将 PAT 存储在 .env 文件中，并在需要时加载
# .env 文件
GITHUB_TOKEN="your_token"
# 然后在终端中加载 .env 文件并使用：
source .env
git clone https://$GITHUB_TOKEN@github.com/your_username/your_repo.git
```

### 使用PAT方式clone到公司服务器上的个人github repo，PAT已过期，如何恢复正常使用git

* 重新生成PAT，一般PAT临近过期时，会发送邮件到注册邮箱，提示重新生成，点击邮箱连接即可重新生成原来的PAT，且权限配置不变

```bash
# 查看之前的repo  URL名称，显示的是旧的已经过期的PAT
cd /path/to/your/repo
git remote -v

# 更新 URL 以包含新的 PAT
git remote set-url origin https://<PAT>@github.com/username/repo.git
# 确保 URL 更新正确，新的repo  URL中包含新PAT即表示更新成功
git remote -v
git pull

# 为了安全性，建议在首次验证后删除 PAT，改用缓存或凭证管理：
git remote set-url origin https://github.com/username/repo.git
git remote -v
# 然后运行以下命令以缓存凭据：
git config --global credential.helper cache
# 之后，Git 会在需要时提示输入用户名和新PAT，并将其临时缓存。
```

## 丢弃本地修改，防止git pull冲突

* 场景描述：
  * 对于同一个git repo中的同一文件tt.py，在A和B电脑上都对该文件分别做了不同的更新。
  * A电脑上的更新提交了git push，且以A为准；
  * B电脑上的更新没有提交git push，因为B电脑上对tt.py的修改仅是临时测试用。
  * 在B电脑上进行git pull操作前，需要先丢弃本地未提交的改动：

```bash
git checkout -- tt.py  # 丢弃本地对 tt.py 的修改
git pull               # 拉取远程更新
```

## 分支管理

### dev分支暂存部分文件，稍晚再merge到master/main分支

* 场景描述：
  * 在公司的gitlab repo A下的一个名为aa的文件夹中，开发维护个人独立项目github repo aa，并定期提交repo aa中的代码给repo A，供team leader审阅代码，目前aa只有一个branch main，后续也以aa repo main branch为标准向公司gitlab repo A提交代码
  * 首先给个人github repo aa新建一个dev branch，dev会包括所有最新的文件，但只会定期选择性合并dev中的部分文件（如file1.py, file2.py）到main branch；对于开发测试中的file3.py，会暂时将该文件的commit记录在dev中维护，暂不merge到main
  * 当file3.py的阶段性版本确定后，将它从dev合并到main，并提交给公司gitlab repo A
* 步骤 1：在个人 repo aa 中创建 dev 分支

```bash
# 切换到 main 分支： 确保当前位于 main 分支
git branch
git checkout main
# 从 main 创建 dev 分支
# 此时，dev 分支与 main 分支内容相同，后续的开发和测试将在 dev 分支中进行。
git checkout -b dev
git branch
```

* 步骤 2：在 dev 分支中进行开发

```bash
# 正常开发和提交： 在 dev 分支中修改代码并提交，例如对 file3.py 进行开发和测试：
# 多次提交： 每次更新 file3.py，都可以继续在 dev 中提交，这些 commit 将记录在 dev 分支历史中。
git add file3.py
git commit -m "Work in progress on file3.py"
# 仅当远程dev分支已经被其他地方更新（如你在另一台电脑上提交了更改）、或其他用户更新，才需要执行git pull --rebase origin dev：
# 当只有自己一个用户在一台电脑上开发时，可以不执行 git pull --rebase origin dev：
git pull --rebase origin dev
git push origin dev

# 在新电脑上获取最新的远程分支（应包括main和dev分支）：
git fetch origin
git branch -a
# 切换到本地 dev 分支并跟踪远程
git checkout -b dev origin/dev
```

* 步骤 3：选择性合并 dev 的部分文件到 main

```bash
# 切换到 main 分支：
git checkout main
# 选择性合并文件（file1.py 和 file2.py）到 main： 使用 git checkout dev -- <file> 命令将文件从 dev 提取到 main：
git checkout dev -- file1.py
git checkout dev -- file2.py
# 查看更改并提交：
# 确认提取的文件内容正确：
git status
git diff
# 提交更改：
git add file1.py file2.py
git commit -m "Merge file1.py and file2.py from dev to main"
git push origin main
```

* 步骤 4：合并 file3.py 到 main（阶段性完成）

```bash
# 切换到 main 分支： 确保在 main 分支：
git checkout main
# 选择性提取 file3.py： 使用 git checkout dev -- file3.py：
git checkout dev -- file3.py
git status
git diff
git add file3.py
git commit -m "Merge stable version of file3.py from dev to main"
# 推送到 GitHub
git push origin main
```

* 步骤 5：将 dev 分支合并到 main 分支

```bash
# 切换到 main 分支：
git checkout main
# 执行合并操作： 将 dev 分支的所有提交合并到 main 中：
git merge dev
# 解决冲突： 如有冲突，需要手动解决冲突，然后再提交：
git status
git add file1.py file2.py file3.py
git commit -m "Merge dev to main"
# 推送到 GitHub
git push origin main

# 合并完成后需要注意的事项
# 同步 main 到 dev 分支（保持一致性）： 如果 main 是主分支，通常在合并后会将最新的 main 同步回 dev，以避免后续开发时两者出现不一致：
git checkout dev
git merge main
# 检查分支状态： 合并完成后，确保两者内容一致：
git diff main dev
# 删除临时分支（可选）： 如果 dev 分支已完成阶段性目标且暂时不需要，可以删除本地或远程的 dev 分支（仅当后续开发不依赖于 dev 时）：
# 删除本地分支：
git branch -d dev
# 删除远程分支：
git push origin --delete dev
```

## 多repo管理

### submodules管理

* 场景描述：
  * repoB 是独立库，repoA 是主项目
  * repoA根目录下git clone repoB，repoB 独立开发，repoA 只需引用特定版本
* **核心要点总结**
  * **子模块是独立的 Git 仓库，记住要在子模块内部做提交**
  * **repoA 只记录 repoB 的 commit SHA，不记录具体代码变更**
  * **推送顺序：先 push 子模块，再 push 主项目**
  * 量化场景建议：为每个策略模块创建独立子模块，便于权限管理和版本回滚

```bash
# 在 repoA 根目录下执行
git submodule add <repoB-url> path/to/repoB
git commit -m "Add repoB as submodule"
```

* 优点：
  * repoB 保持完全独立的版本历史和远程仓库
  * repoA 通过 `.gitmodules` 文件和 commit SHA 精确锁定 repoB 版本
  * 团队克隆时可自动同步：`git clone --recurse-submodules <repoA-url>`
  * 更新 repoB 到新版：`git submodule update --remote`
* 缺点：
  * 操作稍复杂，需额外命令管理
  * 默认子目录为空，需初始化
* 首次添加子模块（在 repoA 中）

```bash
# 1. 进入 repoA 根目录
cd /path/to/repoA

# 2. 添加 repoB 为子模块（指定存放路径）
git submodule add https://github.com/yourname/repoB.git path/to/repoB
# 省略本地路径时path，Git 会使用远程 URL 的基名作为默认目录名（去掉 .git 后缀）
git submodule add git@github.com:yourname/strategies.git
# repoB默认跟踪远程的 main/master 分支。如需指定分支：
git submodule add -b dev https://github.com/yourname/repoB.git repoA/repoB

# 3. 查看生成的 .gitmodules 文件（记录子模块映射）
cat .gitmodules
# 输出示例：
# [submodule "repoB"]
#   path = repoB
#   url = https://github.com/yourname/repoB.git

# 4. 提交配置到 repoA
git add .gitmodules repoB
# 提交 .gitmodules 与子模块“gitlink”
# 这是子模块的“注册表”，记录路径与 URL 的映射关系，会被 Git 跟踪并提交到 repoA 的版本历史中
git add .gitmodules strategies
git commit -m "feat: add repoB as submodule for current project"
git push
```

* 验证命令是否成功

```bash
# 1. 检查 .gitmodules
cat .gitmodules

# 2. 检查子模块状态
git submodule status
# 输出： c3d5a2b... strategies/repoB

# 3. 检查索引类型
git ls-files --stage | grep repoA/repoB
# 输出：160000 c3d5a2b... 0       repoA/repoB

# 4. 检查 repoB 是否可导入
cd repoA
python -c "from repoA.repoB.dual_momentum import run; print('OK')"
```

* 克隆包含子模块的仓库

```bash
# 方式1：克隆时自动初始化所有子模块（推荐）
git clone --recurse-submodules https://github.com/yourname/repoA.git

# 方式2：先克隆再手动初始化（如果忘了加 --recurse-submodules）
git clone https://github.com/yourname/repoA.git
cd repoA
git submodule init      # 初始化本地配置文件
git submodule update    # 拉取子模块代码
```

#### 日常使用操作

* 在 repoA 中更新 repoB 到最新版本

```bash
# 进入子模块目录
cd repoA/repoB

# 拉取 repoB 的最新代码（在 main 分支）
git checkout main
git pull origin main

# 返回主项目并提交更新
cd ../..
git add repoA/repoB  # 这会记录子模块的新 commit SHA
git commit -m "chore: update repoB to latest version"
git push
```

* 在 repoA 中修改 repoB 代码并提交

```bash
# 1. 确保子模块在正确的分支
cd repoA/repoB
git checkout main  # 或开发分支

# 2. 修改代码（例如修改策略参数）
vim repoA/repoB/dual_momentum.py

# 3. 在子模块内提交（提交到 repoB 自己的仓库）
git add .
git commit -m "fix: optimize parameters for Q4 2024"
git push origin main

# 4. 返回主项目，更新子模块指针
cd ../..
git add repoA/repoB
git commit -m "feat: integrate new optimized repoB"
git push
```

* 一键更新所有子模块

```bash
# 拉取所有子模块的最新提交
git submodule update --remote --merge

# 查看状态
git status
# 会显示：modified:   repoA/repoB (new commits)

# 提交更新
git add repoA/repoB
git commit -m "chore: sync all submodules"
```
