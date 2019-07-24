---
title: docker常用命令整理
date: 2019-7-23
tags: docker
---

> 记录一下docker常用的命令，待续...



## 安装

```bash
# 一键安装(linux)docker CE
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
# 启动 Docker CE
sudo systemctl enable docker
sudo systemctl start docker
# 建立 docker 用户组
sudo groupadd docker
sudo usermod -aG docker $USER
# 测试 Docker 是否安装正确
docker run hello-world
# 镜像加速 写入`/etc/docker/daemon.json`
{
	"registry-mirrors": 
	[
		"https://dockerhub.azk8s.cn",
		"https://reg-mirror.qiniu.com"
	]
}
```



## 使用镜像

```bash
# 版本等信息
docker version
# 更多的信息
docker info
# 查看后台运行的容器
docker ps        
# 搜索镜像
docker search ubuntu:18.04
# 下载xxx镜像
docker pull ubuntu:18.04
# 列出镜像
docker image ls
# 中间层镜像
docker image ls -a
# 删除虚悬镜像
docker image prune
# 删除xxx镜像
docker image rm ubuntu 	

# commit保存镜像
# 运行nginx服务
docker run --name webserver -d -p 80:80 nginx
# 对nginx做出修改
docker exec -it webserver bash
root@3729b97e8226:/# echo '<h1>Hello, Docker!</h1>' > /usr/share
/nginx/html/index.html
root@3729b97e8226:/# exit
docker diff webserver
# 保存修改为新镜像
docker commit \
	--author "b1ng0" \
	--message "修改了默认网页" \
	webserver \
	nginx:v2
# 查看镜像历史
docker history nginx:v2
```



## 操作容器

```bash
# 新建并启动容器
docker run -it ubuntu:18.04 /bin/bash
# 启动/重启/停止xxxx容器
docker container start/restart/stop xxx
# 删除xxx容器
docker container rm xxx
# 后台运行
docker run -d ubuntu
# 进入后台运行的容器
docker exec xxx
# 导出容器
docker export xxx > ubuntu.tar
# 导入容器
docker import ubuntu.tar test/ubuntu:v1.0
# 清理所有处于终止状态的容器
docker container prune 							
```



## 访问仓库

```bash
# 注册 https://hub.docker.com
# 登录
docker login # 输入用户名密码
# 退出登录
docker logout 
# 拉取镜像
docker search centos
docker pull centos
# 推送镜像(登陆状态)
docker tag ubuntu:18.04 b1ng0/ubuntu:18.04
docker push b1ng0/ubuntu:18.04
docker search b1ng0
```



## 数据管理

```bash
# 创建数据卷
docker volume create my-vol
# 查看所有数据卷
docker volume ls
# 查看指定数据卷信息
docker volume inspect my-vol
# 启动一个挂载数据卷的容器 (--mount参数后面不要有空格)
docker run -d -P \
	--name web \
	# -v my-vol:/webapp \ 
	--mount source=my-vol,target=/webapp \
	training/webapp \ 
	python app.py
# 查看数据卷(在容器中)的具体信息
docker inspect web
# 删除数据卷
docker volume rm my-vol
# 清理无主数据卷
docker volume prune
# 挂载主机目录作为数据卷
docker run -d -P \
	--name web \
	# -v /src/webapp:/opt/webapp \
	--mount type=bind,source=/src/webapp,target=/opt/webapp \
	training/webapp \
	python app.py
# 挂载单个文件作为数据卷
docker run --rm -it \
	# -v $HOME/.bash_history:/root/.bash_history \
	--mount type=bind,source=$HOME/.bash_history,target=/root/.ba
	sh_history \
	ubuntu:18.04 \
	bash
```



## 使用网络

```bash
# 外部访问容器
# -P 随机映射端口
docker run -d -P training/webapp python app.py  
# 查看应用信息
docker logs container_id
# -p 指定端口映射
# 格式：ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort
docker run -d -p 5000:5000 training/webapp python app.py
# 查看映射端口配置
docker port 433 5000 # 433 是container_id/container_name

# 容器互联
# 新建网络 (-d 指定网络类型 bridge/overlay)
docker network create -d bridge my-net
# 连接容器
docker run -it --rm --name busybox1 --network my-net busybox sh
# 新开终端，连接第二个容器
docker run -it --rm --name busybox2 --network my-net busybox sh
# 在busybox2 容器中ping busybox1, 测试连通性
ping busybox1

# 配置DNS

# 在容器中使用 mount 命令可以看到挂载信息
mount
# 配置全部容器的DNS 写入`/etc/docker/daemon.json`：
{
	"dns" : 
	[
		"114.114.114.114",
		"8.8.8.8"
	]
}
# 检查配置
docker run -it --rm ubuntu:18.04 cat etc/resolv.conf
# 指定容器的配置
docker run -it --rm --dns=114.114.114.114 ubuntu:18.04 

```



## 参考

[Docker — 从入门到实践](https://github.com/yeasy/docker_practice)

