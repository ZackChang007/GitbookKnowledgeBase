## 网络问题
* 禁止wsl2虚拟网卡生成动态ip地址
```bash
sudo vi /etc/wsl.conf
# 写入：
[network]
generateResolvConf = false
```
* 给`/etc/resolv.conf`添加几个有效DNS server
```bash
sudo vi /etc/resolv.conf
# 写入：
# search yourbase.domain.local
# you can find your base domain after running in powershell this ipconfig|findstr DNS-Suffix
nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 1.1.1.1
nameserver 114.114.114.114
```
* 在wsl2 ubuntu中设置host的网络代理：
```bash
sudo vi /etc/environment
# 写入：
http_proxy="http://localhost:7890"
https_proxy="http://localhost:7890"
no_proxy="localhost,127.0.0.1,::1"
ALL_PROXY="socks5://localhost:7890"

# 重启 WSL2 或运行以下命令使更改生效：
source /etc/environment

# 如果希望在每次启动 WSL2 时自动加载这些代理设置，
# 可以将它们添加到你的 ~/.bashrc 或 ~/.zshrc 文件中（根据你使用的 Shell）
# 打开配置文件
nano ~/.bashrc  # 或 nano ~/.zshrc

# 添加代理设置
export http_proxy="http://your_proxy_address:port"
export https_proxy="http://your_proxy_address:port"

# 保存文件后，刷新环境变量
source ~/.bashrc  # 或 source ~/.zshrc

# 检查当前是否有代理配置，可以通过以下命令查看环境变量
echo $http_proxy
echo $https_proxy
# 或者
env | grep -i proxy

# 验证代理是否生效
# 这个命令将返回你当前的外部 IP，如果代理生效，你应该会看到代理服务器的 IP 而不是你本机的 IP。
curl ifconfig.me
```
