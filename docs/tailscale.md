# tailscale

## 配置

### 注册 Tailscale 账号

* 访问 tailscale.com，用 Google/Microsoft/GitHub 账号登录（推荐 GitHub），记下你的 Tailnet 名称（如 user.github）

### 步骤2：家里电脑端配置

* Linux (Ubuntu/Debian)

```bash
# 安装
curl -fsSL https://tailscale.com/install.sh | sh

# 启动并登录
sudo tailscale up

# 看到链接后，复制到浏览器完成授权
```

* 启用 SSH 服务

```bash
# macOS: 系统设置 -> 通用 -> 共享 -> 远程登录（启用）
# Linux: sudo apt install openssh-server && sudo systemctl enable ssh --now
# Windows: 设置 -> 应用 -> 可选功能 -> 添加功能 -> OpenSSH 服务器
```

### 步骤3：手机端配置

* 安装Tailscale app，用同一个Tailscale账号登录

### 步骤4：安装 SSH 客户端

* 安装Termius或者Termux

```bash
# Termux 内直接 SSH
pkg install openssh
ssh username@home-pc.tailnet-name.ts.net  # 或用 Tailscale IP
```

### 步骤5：连接

* ssh连接

```bash
tailscale status

# 输出示例：
# 100.64.0.1  home-pc      user@  linux   active; direct 192.168.1.100:41641, tx 1234 rx 567
# 100.64.0.2  iphone       user@  iOS     active; relay "tok", tx 89 rx 45

ssh user@home-pc
```

* 禁用密钥过期（方便长期访问）:

```bash
# 在 Tailscale 控制台 -> Machines -> 点击设备 -> Disable key expiry
# 这样不需要定期重新授权
```

* 连接不上怎么办

```bash
# 检查状态
tailscale status

# 重新登录
sudo tailscale up --force-reauth

# 查看日志
sudo tailscale bugreport
```
