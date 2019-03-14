---
title: pip修改官方源踩的坑
tags: python
---
## linux篇：
* 编辑配置文件（如果没有, 新建一份）：
`vi ~/.pip/pip.conf`
* 在配置文件内加上（这里使用豆瓣源）:
```
[global]
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com
```
* 然后就可以愉快地：
`pip install xxxxx`

## windows篇（比较奇葩）：
* 新建文件（pip文件夹与pip.ini都要自己新建）：
`C:\Users\用户名\pip\pip.ini`
注意：不是C:\Users\用户名\AppData\Local\pip下的 pip.ini
* 在配置文件内加上（这里使用豆瓣源）:
```
[global]
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com
```
* 然后就可以愉快地：
`pip install xxxxx`

## 参考链接：
https://www.v2ex.com/t/291817
https://ficapy.github.io/2013/12/27/pip_use_china_mirror/