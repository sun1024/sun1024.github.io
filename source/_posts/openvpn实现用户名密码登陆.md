---
title: openvpn实现用户名密码登陆
date: 2019-2-24 22:10
tags: linux
---
## openvpn实现用户名密码登陆

### 0x00 openvpn安装

网上教程一堆，这里采用懒人傻瓜式安装方式，感谢大佬的脚本：https://github.com/Nyr/openvpn-install.

> bash openvpn-install.sh

然后一路回车不到一分钟即可搭建好一个openVPN服务器。。。

### 0x01 服务端配置

在server.conf中添加如下内容

> vim /etc/openvpn/server.conf

```shell
auth-user-pass-verify /etc/openvpn/checkpsw.sh via-env
username-as-common-name
script-security 3 execve
```

在/etc/openvpn目录下添加文件checkpsw.sh:

> vim /etc/openvpn/checkpsw.sh

```shell
#!/bin/sh
###########################################################
#checkpsw.sh (C) 2004 Mathias Sundman <mathias@openvpn.se>
#
# This script will authenticate OpenVPN users against
# a plain text file. The passfile should simply contain
# one row per user with the username first followed by
# one or more space(s) or tab(s) and then the password.

PASSFILE="/etc/openvpn/psw-file"
LOG_FILE="/etc/openvpn/openvpn-password.log"
TIME_STAMP=`date "+%Y-%m-%d %T"`

###########################################################

if [ ! -r "${PASSFILE}" ]; then
  echo "${TIME_STAMP}: Could not open password file \"${PASSFILE}\" for reading." >> ${LOG_FILE}
  exit 1
fi

CORRECT_PASSWORD=`awk '!/^;/&&!/^#/&&$1=="'${username}'"{print $2;exit}' ${PASSFILE}`

if [ "${CORRECT_PASSWORD}" = "" ]; then
  echo "${TIME_STAMP}: User does not exist: username=\"${username}\", password=\"${password}\"." >> ${LOG_FILE}
  exit 1
fi

if [ "${password}" = "${CORRECT_PASSWORD}" ]; then
  echo "${TIME_STAMP}: Successful authentication: username=\"${username}\"." >>${LOG_FILE}
  exit 0
fi

echo "${TIME_STAMP}: Incorrect password: username=\"${username}\", password=\"${password}\"." >> ${LOG_FILE}
exit 1
```

给予执行权限：

> chmod 755 /etc/openvpn/checkpsw.sh

在/etc/openvpn目录下添加用户名密码文件psw-file:

> vim /etc/openvpn/psw-file

```shell
user1 pass1 # 用户名 密码以空格隔开
user2 pass2
```

安全起见设成只读：

> chmod 400 /etc/openvpn/psw-file   

重启服务：

> service openvpn restart

### 0x02 客户端配置

在服务器安装openvpn时生成的client.ovpn末尾加入一行：

```
auth-user-pass
```

重新导入openvpn GUI即可使用用户名密码登陆.

### 0x03 坑点

使用openvpn-install.sh安装时，选择TCP(默认)方式无法使用用户名密码登陆，选择UDP则没有问题。