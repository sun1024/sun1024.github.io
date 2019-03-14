---
title: ubuntu16.04单网卡配置多ip
tags: linux
---
## ubuntu16.04单网卡配置多ip

- 环境：ubuntu16.04

> vim /etc/network/interfaces

- 默认配置：

```shell
##lo配置 
auto lo 
iface lo inet loopback 
##网卡eth0的配置 
auto eth0 
iface eth0 inet dhcp 
```

- 双ip配置：

```shell
##lo配置 
auto lo 
iface lo inet loopback 
##虚拟出一个eth0:0 
auto eth0 
auto eth0:0 
##配置eth0的ip,默认网关,子网掩码 
iface eth0 inet static 
address 192.168.1.23 
gateway 192.168.1.1 
netmask 255.255.0.0 
##配置eth0:0的ip,默认网关,子网掩码 
iface eth0:0 inet static 
address 192.168.1.24 
gateway 192.168.1.1 
netmask 255.255.255.0 
```

- 多ip配置：

```shell
##lo配置 
auto lo 
iface lo inet loopback 
##虚拟出两个：eth0:0和eth0:1 
auto eth0 
auto eth0:0 
auto eth0:1 
##配置eth0的ip,默认网关,子网掩码 
iface eth0 inet static 
address 192.168.1.23 
gateway 192.168.1.1 
netmask 255.255.0.0 
##配置eth0:0的ip,默认网关,子网掩码 
iface eth0:0 inet static 
address 192.168.1.24 
gateway 192.168.1.1 
netmask 255.255.255.0 
##配置eth0:1的ip,默认网关,子网掩码 
iface eth0:1 inet static 
address 192.168.1.25 
gateway 192.168.1.1 
netmask 255.255.255.0 
```

- 重启网络服务

>  $sudo service networking restart 
> 或者sudo /etc/init.d/networking restart 