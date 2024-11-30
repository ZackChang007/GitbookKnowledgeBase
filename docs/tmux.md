# tmux
* Ref: 
  * [轻松玩转 Tmux](https://www.wolai.com/stupidccl/tV4zUjv3G8ufVDqeXY4fck)
## 设置alias
* 以下内容粘贴到/.bashrc或~/.zshrc文件中
```bash
# 新建
alias tnew="tmux new -s "
# 列出会话(ctrl+b s)
alias tls="tmux ls"
# 退出会话(ctrl+b d)
alias tout="tmux detach"
# 进入会话
alias tin="tmux attach -t "
# 杀死指定会话
alias tkill="tmux kill-session -t "
# 杀死全部会话
alias tkillall="tmux kill-server"
# 上下划分窗格
alias tsud="tmux split-window"
# 左右划分窗格
alias tslr="tmux split-window -h"
# 光标上移
alias tu="tmux select-pane -U"
# 光标下移
alias td="tmux select-pane -D"
# 光标左移
alias tl="tmux select-pane -L"
# 光标右移动
alias tr="tmux select-pane -R"
# 切换会话
alias tswitch="tmux switch -t "
# 重命名会话(ctrl+b $)
alias trename="tmux rename-session -t "
```
* 保存文件并执行`source ~/.bashrc`或`source ~/.zshrc`使设置生效
## 使用
* 新建会话：
  * 在普通终端，运行`tnew test`，即可进入新建的tmux test会话
  * 退出该tmux会话：`tout`
  * 回到普通终端，创建新的tmux会话，运行`tnew test1`
* 列出会话：`tls`
* 进入、退出会话：
  * 进入会话：`tin test`
  * 退出会话：
    * `tout`
    * `exit`, 退出同时kill掉当前会话
    * `ctrl+b d`, 貌似不光会退出当前会话(session)，还会同时杀死当前会话
* 杀死会话：`tkill test`或`tkillall`
* 划分窗格：
  * 上下划分窗格：进入某个tmux会话，`tsud`
  * 左右划分窗格：进入某个tmux会话，`tslr`
* 光标在不同窗口之间移动
  * 光标上移：`tu`
  * 光标下移：`td`
  * 光标左移：`tl`
  * 光标右移：`tr`
* 切换会话：`tswitch test`
