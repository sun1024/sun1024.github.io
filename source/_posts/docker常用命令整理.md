---
title: docker常用命令整理
date: 2019-7-23
tags: docker
---

> 记录一下docker常用的命令，待续...



## 安装

```shell
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



## 镜像操作

```shell
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
```



## 容器操作

```shell
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



## 参考

[Docker — 从入门到实践]('https://github.com/yeasy/docker_practice')