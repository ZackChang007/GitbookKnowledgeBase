# 基础操作
- https://www.imooc.com/video/14624
## image镜像
### 打开docker daemon
### 查看当前docker images
1. `docker images`
    - image镜像只读
    - container容器可读写，当需要修改image中的文件时，先把文件拷贝到container中再修改
### pull hello world image
1. `docker pull hello-world:latest`
    - pull的时候可以指定image的具体tag(版本)，如不指定默认为latest
## container容器
### docker run
1. help
    `docker run --help`
2. `docker run [OPTIONS] IMAGE[:TAG] [COMMAND] [ARG...]`
    - IMAGE: 镜像名称
    - TAG: 镜像的标记、版本
    - COMMAND: 镜像run起来后需要执行的命令
    - ARG: COMMAND命令依赖的参数
    - OPTIONS：run的一些选项，如'-d'代表在后台运行并打印出image的48位独有id
    - `docker run hello-world`
3. 查看docker容器运行状态
    - `docker ps`   
4. 在运行的容器中执行一个命令
    - `docker exec --help`    
    - `docker exec -i`，使命令输入保持开启，即使容器是后台运行状态
    - `docker exec -t`，分配一个伪终端，搭配'-i'参数使用，从而可以输入命令
5. 在持续运行的docker容器nginx内执行命令
   ```shell script
   docker pull nginx
   # 在docker hub中pull nginx image
   
   docker images
   # IMAGE ID本来是48位唯一的，只截取显示了后12位
   >
   REPOSITORY                       TAG       IMAGE ID       CREATED        SIZE
   docker101tutorial                latest    19c5413ecf56   2 days ago     27.4MB
   zackchang585/docker101tutorial   latest    19c5413ecf56   2 days ago     27.4MB
   alpine/git                       latest    8bfbb50cd816   12 days ago    43.4MB
   nginx                            latest    1db0b6ded6ab   2 weeks ago    135MB
   hello-world                      latest    46331d942d63   7 months ago   9.14
   # 后台运行hello-world容器，并打印出其48位独有id
   > 
   579fc3276756d46230510c75d41903baac82f90195b652e4076e451d2f066663
   
   docker ps
   # 查看正在运行的docker的状态，print status
   >
   CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
   579fc3276756   nginx     "/docker-entrypoint.…"   35 seconds ago   Up 35 seconds   80/tcp    stupefied_pare

   docker exec -it 579 bash
   # 因只有一个容器在运行，直接输入其id前几位就可以自动定位到该容器
   # 命令表示在nginx容器中打开一个bash窗口，从返回的"root@579fc3276756"可知返回正常
   # 可以在打开的容器bash内，输入正常的linux命令如"ls"、"pwd"等
   >
   root@579fc3276756:/# 
   
   exit
   # 退出nginx容器bash，回到主机
   >
   (base) admin@admindeMacBook-Pro-6 ~ %
   ```
## docker网络
### 网络类型
- https://www.imooc.com/video/14623
#### docker网络隔离原理
+ docker底层是linux技术，通过namespace进行隔离，包括网络
#### docker网络分类
1. Bridge
    - 创建docker时默认使用独立的桥接模式，区别于主机网络
2. Host
    - 启动容器时，指定使用主机网络，则容器不会创建Bridge模式的namespace和配置独立的路由、网卡等
3. None
    - docker没有网络，适用于一些安全防护场景
#### 在nginx容器中配置Bridge网络
```shell script
docker stop 579
# 关闭nginx容器运行

docker run --help
# 查看网络相关的指令帮助 

docker run -d -p 8080:80 nginx
# -d, detached, 容器在后台运行
# -p 8080:80,注意p小写，前一个8080为主机端口，后一个80是容器端口(nginx默认端口)
> 
68a31cbcf7213b0404c4c9454a77f484e9cff5ef5332a7a3692a9d89eb1ee7a4

docker ps
# 检查容器运行状态
> 
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
68a31cbcf721   nginx     "/docker-entrypoint.…"   50 seconds ago   Up 49 seconds   0.0.0.0:8080->80/tcp   peaceful_mestorf

netstat -na|grep 8080
# 检查网络端口状态，8080已经是listen状态
>
tcp46      0      0  *.8080                 *.*                    LISTEN

打开本机网页浏览器输入"localhost:8080", 应该能看到"welcome to nginx"字样

docker stop 68a 

docker run -d -P nginx
# -P，注意P大写，表示把所有容器网络端口随机映射到主机端口
>
7c52ad9eccb52595d879f9a94ecb40a732d0afdf13b8c735702cbae987d89b7d

docker ps
# 主机随机端口55000映射到容器80端口
>
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                   NAMES
7c52ad9eccb5   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:55000->80/tcp   peaceful_franklin

netstat -na|grep 55000
# 主机55000端口已经是listen状态
>
tcp46      0      0  *.55000                *.*                    LISTEN 

打开本机网页浏览器输入"localhost:55000", 应该能看到"welcome to nginx"字样

docker stop 7c52
```          
#### 把容器网络配置为host
- https://weread.qq.com/web/reader/93d325a0719b200493d5ba9kc1632f5021fc16a5320f3dc
```shell script
docker ps

docker network ls
>
NETWORK ID     NAME                  DRIVER    SCOPE
0ddd9850cad0   bridge                bridge    local
c190dd4757e1   ft_userdata_default   bridge    local
999e8b94d217   host                  host      local
97c79d69147e   none                  null      local

docker run -itd --network=host nginx
# -i, 允许在容器中交互，即使容器后台运行；-t，生成伪终端允许在容器中输入命令；-d，后台运行
>
92842d918c09dbe405bb0e1c30ce099419a245b51a401a70c85db9487c6e1954

docker stop 928
```
#### 在一个docker容器中检查其网络状态
```shell script
docker run -d nginx
>
59f557f1dde9becf7c61980ef6048bab2891fba33f4a178120053594202d634a

docker ps
>
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
59f557f1dde9   nginx     "/docker-entrypoint.…"   4 seconds ago   Up 4 seconds   80/tcp    sleepy_lalande

docker exec -it 59 bash
>
root@59f557f1dde9:/#

# 因为显示不支持ping命令，先安装ping依赖包
root@59f557f1dde9:/# apt-get update
root@59f557f1dde9:/# apt-get install iputils-ping

ping www.baidu.com

exit
```

## 制作自己的镜像image
- https://yeasy.gitbook.io/docker_practice/image/build

### Dockerfile
