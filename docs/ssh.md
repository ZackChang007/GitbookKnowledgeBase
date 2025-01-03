# ssh
## 在windows terminal中使用ssh连接远程服务器
```bash
# 查看有哪些ssh config
# dir 是 Windows 中的内置命令，可以在当前目录及其子目录中查找文件或文件夹
# /s：搜索当前目录及其所有子目录, /p：分页显示结果，避免结果过多时一屏显示不下。
dir "known_hosts" /s /p
# 找到并返回.ssh文件夹的known_hosts文件所在路径，C:\Users\UserName\.ssh
cd C:\Users\UserName\.ssh
dir

# 打开C:\Users\UserName\.ssh\config文件，查看可连接的ssh server
# 如果密钥配置好，一般可以直接连接成功
ssh server1
```
## 生成ssh pub key
```bash
# 生成ssh密钥对
ssh-keygen -t ed25519 -C '邮箱名 其他标识性字段'
# 如：
ssh-keygen -t ed25519 -C "your_email@example.com - Workstation1 - ProjectABC"

# 输入保存密钥对的路径，默认路径是 ~/.ssh/id_ed25519
# 输入保存密钥对的密码，密码用于解密私钥
# 成功后会在 ~/.ssh/ 下生成 id_ed25519 和 id_ed25519.pub 两个文件

# 将公钥上传到远程服务器
# 登录远程服务器，将公钥文件 id_ed25519.pub 上传到 ~/.ssh/authorized_keys 文件中
# 或者直接将公钥内容追加到 ~/.ssh/authorized_keys 文件中

# 尝试连接远程服务器
ssh server1
```
