# K-Bar数据同步配置指南

## 概述
本指南详细介绍如何使用Syncthing在Windows环境下实现K-Bar数据的点对点增量同步，确保公司电脑与本地电脑之间的CSV文件实时同步。

## 环境要求
- Windows 10/11操作系统（公司电脑和本地电脑）
- 稳定的网络连接
- 管理员权限（用于安装软件）

## 步骤一：准备工作

### 1.1 确认数据目录结构
在公司电脑上确认K-Bar数据的存储结构：
```
K-Bar数据根目录/
├── 股票数据/
│   ├── 600519.sh.csv
│   ├── 000001.sz.csv
│   └── ...
├── 期货数据/
│   ├── RB2410.csv
│   └── ...
└── 其他资产类别/
    └── ...
```

### 1.2 记录重要信息
- 公司电脑K-Bar数据根目录路径：____________
- 本地电脑目标同步目录路径：____________
- 公司电脑计算机名：____________
- 本地电脑计算机名：____________

## 步骤二：安装Syncthing

### 2.1 公司电脑安装

#### 方案一：使用Windows安装包（推荐）
1. 访问GitHub发布页：https://github.com/Bill-Stewart/SyncthingWindowsSetup/releases
2. 下载最新版本：`syncthing-windows-setup.exe`
3. **重要**：如果遇到"Setup initialization error: WSH script registration is not valid"错误，请按以下步骤解决：

   **解决方法**：
   1. 以管理员身份打开命令提示符(CMD)
   2. 运行以下命令重新注册WSH：
      ```cmd
      regsvr32 %systemroot%\system32\vbscript.dll
      regsvr32 %systemroot%\system32\jscript.dll
      regsvr32 %systemroot%\system32\wshom.ocx
      regsvr32 %systemroot%\system32\wshext.dll
      ```
   3. 如果上述命令失败，尝试：
      ```cmd
      regsvr32 /u %systemroot%\system32\vbscript.dll
      regsvr32 %systemroot%\system32\vbscript.dll
      ```
   4. 重启电脑后重新运行安装程序

4. 如果仍然无法解决，使用**方案二**（便携版）

#### 方案二：使用便携版（备用方案）
1. 访问Syncthing官网：https://syncthing.net/
2. 下载Windows便携版：点击"Download" → 选择"Windows" → 下载"Syncthing for Windows (x64)"
3. 解压下载的压缩包到：`C:\Program Files\Syncthing\`
4. 创建桌面快捷方式：
   - 右键`syncthing.exe` → 发送到 → 桌面快捷方式
   - 重命名为"Syncthing-公司电脑"

### 2.2 本地电脑安装
重复上述步骤，解压到：`C:\Program Files\Syncthing\`，创建快捷方式"Syncthing-本地电脑"

## 步骤三：网络连接方案选择

**重要说明**：ToDesk的"网络设置"仅提供代理服务器配置，**没有"远程局域网"功能**。因此需要采用以下方案实现Syncthing连接：

### 方案一：使用Syncthing自带穿透（推荐）
**适用场景**：双方均可访问公网，允许出站连接

#### 公司电脑配置：
1. 安装并运行Syncthing
2. 在Syncthing设置中确认以下选项已启用：
   - **全局发现**（Global Discovery）✓
   - **NAT遍历**（NAT traversal）✓
   - **中继**（Relaying）✓
3. 防火墙放行端口：
   - TCP 22000（主要传输端口）
   - UDP 22000（QUIC传输，可选）
   - UDP 21027（本地发现，可选）

#### 本地电脑配置：
1. 同样启用上述三个选项
2. 防火墙放行相同端口
3. 在Syncthing中添加公司电脑设备ID

**特点**：Syncthing会优先尝试直连，无法直连时自动使用官方中继服务器

### 方案二：使用叠加网络（Tailscale/Zerotier）
**适用场景**：公司网络限制较多，或希望获得固定内网地址

#### 以Tailscale为例：
1. **公司电脑**：
   - 安装Tailscale并登录账号
   - 获取100.x.x.x虚拟IP地址
   - 在Syncthing监听地址中添加：`tcp://100.x.x.x:22000`

2. **本地电脑**：
   - 安装Tailscale并登录同一账号
   - 获取虚拟IP地址
   - 添加公司电脑Tailscale IP到Syncthing对端地址

**特点**：两台电脑处于同一虚拟内网，Syncthing可直连

### 方案三：端口转发/反向代理
**适用场景**：一端有公网IP或VPS

#### 配置方法：
1. **有公网IP的一端**：
   - 在路由器设置端口转发：将外部22000端口映射到内网电脑22000
   - 或在VPS上部署FRP，将流量转发到内网

2. **Syncthing配置**：
   - 在无公网IP的电脑Syncthing中，设置对端地址为：`tcp://公网IP:22000`

### 方案四：自建Syncthing中继
**适用场景**：官方中继不可用或需要完全自控

#### 配置方法：
1. 在有公网的服务器上部署`strelaysrv`
2. 在两端Syncthing中指定自建中继地址
3. 参考官方文档配置认证与限速

**注意**：此方案需要服务器资源和维护成本

## 步骤四：配置Syncthing

### 4.1 启动Syncthing服务

#### 公司电脑：
1. 双击"Syncthing-公司电脑"快捷方式
2. 浏览器自动打开`http://localhost:8384`
3. 首次运行时，记录设备ID（页面顶部显示）

#### 本地电脑：
1. 双击"Syncthing-本地电脑"快捷方式
2. 浏览器自动打开`http://localhost:8384`
3. 记录设备ID

### 4.2 设备配对（建立集群）

#### 在本地电脑获取设备ID：
1. 在本地电脑的Syncthing管理界面中
2. 点击顶部"操作"菜单 → 选择"显示ID"
3. 复制显示的56位设备ID

#### 在公司电脑添加远程设备：
1. 在公司电脑的Syncthing管理界面中
2. 点击左侧"远程设备"菜单 → 点击"添加设备"
3. 在弹出的窗口中，将刚才复制的本地设备ID粘贴到"设备ID"框中
4. 为设备起个名字（如"本地电脑"），方便识别
5. 点击"保存"

#### 验证配对成功：
1. 等待几秒钟，如果连接成功
2. 公司设备的"远程设备"列表中会显示本地设备名称
3. 旁边会有绿色小圆点，表示两台设备已成功配对

### 4.3 配置同步文件夹

#### 在公司电脑添加共享文件夹：
1. 在Syncthing Web界面点击"添加文件夹"
2. 配置参数：
   - 文件夹标签：`K-Bar数据`
   - 文件夹路径：`D:\数据\K-Bar\`（根据实际路径调整）
   - 文件夹ID：`kbar-data`（自定义，需记住）
3. 在"共享"选项卡中，勾选刚才添加的本地设备
4. 高级设置：
   - 忽略权限：✓（建议勾选）
   - 监视更改：✓（启用实时监控）
   - 文件版本控制：选择"无版本控制"
5. 点击"保存"

#### 在本地电脑接受共享：
1. 在本地电脑Syncthing界面，会收到共享请求通知
2. 点击"添加"接受请求
3. 配置接收文件夹：
   - 文件夹标签：`K-Bar数据-本地`
   - 本地路径：`E:\同步数据\K-Bar\`（选择本地目标路径）
   - 保持相同的文件夹ID：`kbar-data`
4. 点击"保存"

## 步骤五：优化同步性能

### 5.1 网络优化
1. 在Syncthing设置 → 连接：
   - 启用"启用NAT遍历"
   - 启用"本地发现"
   - 启用"全局发现"
   - 设置"最大发送速率"：0（无限制）
   - 设置"最大接收速率"：0（无限制）

### 5.2 文件夹优化
1. 编辑K-Bar数据文件夹设置
2. 高级选项：
   - 重新扫描间隔：60秒（减少扫描频率）
   - 监视更改：启用（实时监控文件变化）
   - 忽略模式：添加以下规则：
     ```
     // 忽略临时文件
     *.tmp
     *.temp
     ~*
     
     // 忽略日志文件
     *.log
     
     // 忽略系统文件
     .DS_Store
     Thumbs.db
     ```

### 5.3 设备优化
1. 在设备设置中：
   - 压缩：启用（减少网络传输）
   -  introducer：公司电脑启用，本地电脑禁用
   - 自动接受：本地电脑启用

## 步骤六：验证同步功能

### 6.1 初始同步测试
1. 在公司电脑创建一个测试CSV文件：`test_20241113.csv`
2. 添加一些测试数据
3. 观察Syncthing界面：
   - 公司电脑：显示"正在同步"状态
   - 本地电脑：显示"接收中"状态
4. 验证文件是否出现在本地目标目录

### 6.2 增量更新测试
1. 在公司电脑修改现有CSV文件（如600519.sh.csv）
2. 在文件末尾添加新数据行
3. 保存文件
4. 观察同步状态：
   - 应该显示"已同步"或"同步完成"
   - 本地文件应该实时更新

### 6.3 大文件测试
1. 复制一个较大的CSV文件（>100MB）到同步目录
2. 监控同步进度和时间
3. 验证传输速度和完整性

## 步骤七：日常监控和维护

### 7.1 监控界面
- 公司电脑：访问`http://localhost:8384`
- 本地电脑：访问`http://localhost:8384`

### 7.2 关键指标监控
1. 同步状态：绿色表示正常，红色表示错误
2. 同步速度：显示当前传输速率
3. 文件数量：显示已同步文件总数
4. 存储空间：显示本地磁盘使用情况

### 7.3 日志查看
1. 点击"操作" → "日志"
2. 查看最近的同步活动
3. 关注错误和警告信息

## 常见问题和解决方案

### 8.1 连接问题
**问题**：两台电脑无法建立连接
**解决**：
1. 检查网络连接方案是否配置正确
2. 确认防火墙允许Syncthing端口（22000）
3. 检查两台电脑的Syncthing设备ID是否正确

### 8.2 同步速度慢
**问题**：文件同步速度很慢
**解决**：
1. 检查网络带宽使用情况
2. 调整Syncthing的并发连接数
3. 启用压缩功能
4. 考虑在非工作时间进行大批量同步

### 8.3 文件冲突
**问题**：出现文件版本冲突
**解决**：
1. 由于K-Bar数据是只追加模式，通常不会出现冲突
2. 如发生冲突，Syncthing会创建冲突副本
3. 手动合并冲突文件，删除冲突副本

### 8.4 权限错误
**问题**：显示权限被拒绝
**解决**：
1. 确保Syncthing以管理员权限运行
2. 检查目标文件夹的NTFS权限
3. 在Syncthing设置中启用"忽略权限"

### 8.5 WSH脚本注册错误
**问题**：安装时出现"Setup initialization error: WSH script registration is not valid"
**解决**：
1. 以管理员身份运行CMD，执行：
   ```cmd
   regsvr32 %systemroot%\system32\vbscript.dll
   regsvr32 %systemroot%\system32\jscript.dll
   regsvr32 %systemroot%\system32\wshom.ocx
   regsvr32 %systemroot%\system32\wshext.dll
   ```
2. 如果无效，使用便携版方案（见2.1节的方案二）

### 8.6 网络连接方案选择
**问题**：不确定使用哪种网络连接方案
**解决**：
1. **优先尝试方案一**（Syncthing自带穿透）
2. **如果公司网络限制严格**，使用方案二（Tailscale/Zerotier）
3. **如果有公网IP或VPS**，考虑方案三（端口转发）
4. **如果需要完全自控**，选择方案四（自建中继）

## 性能优化建议

### 9.1 定期维护
1. 每月清理Syncthing数据库：
   - 设置 → 高级 → 清理数据库
2. 检查磁盘空间使用情况
3. 优化忽略模式规则

### 9.2 备份策略
1. 定期备份Syncthing配置
2. 导出设备ID和文件夹配置
3. 建立备用同步路径

### 9.3 监控告警
1. 设置磁盘空间告警阈值
2. 监控同步失败告警
3. 配置邮件通知（可选）

## 附录

### A. 常用命令
```bash
# 查看Syncthing状态
http://localhost:8384/rest/system/status

# 重启Syncthing服务
# 在Windows服务管理器中重启Syncthing服务
```

### B. 配置文件位置
```
公司电脑：C:\Users\[用户名]\AppData\Local\Syncthing\
本地电脑：C:\Users\[用户名]\AppData\Local\Syncthing\
```

### C. 技术支持
- Syncthing官方文档：https://docs.syncthing.net/
- 社区论坛：https://forum.syncthing.net/
- GitHub Issues：https://github.com/syncthing/syncthing/issues

### D. 防火墙配置参考
```bash
# Windows防火墙命令（管理员CMD）
netsh advfirewall firewall add rule name="Syncthing TCP" dir=in action=allow protocol=TCP localport=22000
netsh advfirewall firewall add rule name="Syncthing UDP" dir=in action=allow protocol=UDP localport=22000
netsh advfirewall firewall add rule name="Syncthing Discovery" dir=in action=allow protocol=UDP localport=21027
```

---

**配置完成确认清单**
- [x] Syncthing在公司电脑正常运行
- [x] Syncthing在本地电脑正常运行
- [x] 设备配对成功（绿色圆点显示）
- [x] 共享文件夹配置完成
- [x] 测试文件同步成功
- [ ] 增量更新测试通过
- [ ] 监控界面可正常访问
- [ ] 备份策略已制定

**最后更新时间：2024年11月13日**