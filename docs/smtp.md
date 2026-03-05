# smtp邮箱设置

## qq邮箱设置

* `sudo apt update`,`sudo apt install s-nail`,`sudo vim /etc/s-nail.rc`，并填写如下：

```text
# 必须设置，以启用新语法
set v15-compat

# 发件人信息
set from="你的QQ号@qq.com"

# SMTP 服务器配置 (关键修改！将用户名和授权码直接写在 URL 中)
# 注意：这里的"你的授权码"请替换为你的QQ邮箱授权码
set mta=smtps://你的QQ号%40qq.com:你的授权码@smtp.qq.com:465

# 服务器认证方式
set smtp-auth=login

# (可选) 等待发送结果，而不是后台发送
set sendwait
```

* 测试：`cat ~/testqq.txt | s-nail -s "test_qq_mail" -v 你的QQ号@qq.com`
* crontab: `59 11 * * * cat ~/testqq.txt | s-nail -s "testqq" -v 你的QQ号@qq.com`
