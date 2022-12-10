# mannual
## 把本地项目发布到github
```
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


