# tmux
* Ref: 
  * [轻松玩转 Tmux](https://www.wolai.com/stupidccl/tV4zUjv3G8ufVDqeXY4fck)
  * [.tmux](https://github.com/gpakosz/.tmux)
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
## 组合键
```bash
############## 面板管理 ##############
Ctrl + a + %  # 水平分割窗口
Ctrl + a + "  # 垂直分割窗口"
Ctrl + a + o  # 在当前窗口中切换到下一个面板
Ctrl + a + x  # 关闭当前面板（等同于 tmux kill-pane）
Ctrl + a + 空格  # 切换面板布局（比如平铺、均分等）
Ctrl + a + z  # 放大/还原当前面板（当前面板全屏显示）

############## 窗口管理 ##############
Ctrl + a + c  # 创建新窗口
Ctrl + a + ,  # 重命名当前窗口
Ctrl + a + w  # 列出当前会话中的所有窗口
Ctrl + a + &  # 关闭当前窗口（等同于 tmux kill-window）

############## 会话管理 ##############
Ctrl + a + d  # 将当前会话分离，返回到普通终端（等同于 detach）
Ctrl + a + s  # 列出所有会话，方便选择连接
Ctrl + a + $  # 重命名当前会话

############## 复制模式 ##############
Ctrl + a + [  # 进入复制模式，用于滚动查看历史输出
Ctrl + a + ]  # 粘贴复制模式的内容
Ctrl + a + Ctrl + f  # 在复制模式中向前搜索
Ctrl + a + Ctrl + b  # 在复制模式中向后搜索

############## 多个会话的操作 ##############
Ctrl + a + :  # 打开 tmux 命令提示符，输入命令直接控制会话
Ctrl + a + t  # 显示时钟
Ctrl + a + ?  # 列出所有 tmux 绑定快捷键

############## 其他 ##############
ctrl+a [0-9]  # 切换同一会话(session)的不同窗口(window)
```
