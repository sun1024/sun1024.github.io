---
title: go get速度优化
date: 2019-11-19
tags: go
---
## go get 速度慢

 go get -u github.com/gpmgo/gopm 

将 go get 替换成gopm get -g

对于下载失败的 直接通过github clone

eg:

mkdir -p $GOPATH/src/golang.org/x

cd $GOPATH/src/golang.org/x

git clone https://github.com/golang/sys.git

## git clone 速度慢

设置全局socks5代理

 git config --global http.proxy socks5://your-server:your-port 

取消设置

 git config --global --unset http.proxy 

## 使用socks代理

apt install tsocks
vim /etc/tsocks.conf

```shell
local = 192.168.1.0/255.255.255.0  #local表示本地的网络，也就是不使用socks代理的网络
local = 127.0.0.0/255.0.0.0
server = 127.0.0.1   #socks服务器的IP
server_type = 5  #socks服务版本
server_port = 1080  ＃socks服务使用的端口
```

使用代理：

tsocks apt-get install XXX

tsocks wget XXX

