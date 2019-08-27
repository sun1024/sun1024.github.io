---
title: vmware彻底关闭时间同步
date: 2019-8-27
tags: vmware
---
# 0x01 问题

迫于某垃圾项目需要在一个2014年的win7虚拟机中进行开发，宿主机时间不在2014年虚拟机里面的软件即会崩溃，但是调到2014年宿主机就不能上网了，作为一个复制粘贴boy，实在不能忍受断网调代码，然而在vmware上直接关闭时间同步，虚拟机依然会不时的与宿主机同步时间，于是在虚拟机崩了无数次之后，终于找到了解决方法。。。



# 0x02 解决方法

1. 在虚拟机的 .vmx 文件中添加配置选项:

   ```
   tools.syncTime = "FALSE"
   time.synchronize.continue = "FALSE"
   time.synchronize.restore = "FALSE"
   time.synchronize.resume.disk = "FALSE"
   time.synchronize.shrink = "FALSE"
   time.synchronize.tools.startup = "FALSE"
   time.synchronize.tools.enable = "FALSE"
   time.synchronize.resume.host = "FALSE"
   ```

2. 在win7中关闭与Internet时间服务器同步

   ![1566871209850](/images/1566871209850.png)



# 0x03 参考链接

https://kb.vmware.com/articleview?docid=1189&lang=zh_CN