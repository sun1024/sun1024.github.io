---
title: OAI搭建eNB
date: 2019-12-12
tags: 5g
---
## 0x00 前言
难以置信，又开始搞5g了。。。

## 0x01 准备

参考链接： https://blog.csdn.net/qq_42030961/article/details/82740296 

安装环境：

 Ubuntu 14.04.3 

 USRP B210 

## 0x02 安装步骤

### 更换内核

执行如下两条，更换3.19.0-61低延迟内核

> sudo apt-get update
> sudo apt-get install linux-image-3.19.0-61-lowlatency linux-headers-3.19.0-61-lowlatency

更换完成后输入

> sudo reboot

电脑就会立刻重启了。重启后输入 uname -a可以查看内核信息。如下

> Linux hostname 3.19.0-61-lowlatency #69~14.04.1-Ubuntu SMP PREEMPT Thu Jun 9 10:15:00 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

### 电源管理

> sudo gedit /etc/default/grub

在GRUB_CMDLINE_LINUX_DEFAULT="quiet splash”这行的下面添加两行：

> GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_pstate=disable"
> GRUB_CMDLINE_LINUX_DEFAULT="processor.max_cstate=1 intel_idle.max_cstate=0 idle=poll”

预告：如果没有关掉c-state，这两行会需要修改，先往下走。

> sudo gedit /etc/modprobe.d/blacklist.conf

在文件最后添加

> blacklist intel_powerclam

依次执行

> sudo apt-get install cpufrequtils
> sudo gedit /etc/default/cpufrequtils

这个cpufrequtils 大概率为空文件，在里面加上一句：

> GOVERNOR=“performance”

> sudo update-rc.d ondemand disable

> sudo apt-get install i7z

安装i7z，后面可以查看CPU频率。


重启，进入bios关闭与节能或者影响CPU次能性能的设置，一般在Advanced设置里面。关闭超线程（Hyper-threading），C-state（有的电脑在bios里面找不到c-state，比如我的就没有，没有需要强行在grub里关），方法见（8）：

用i7z查看是否完成操作

sudo i7z
看到所有频率都在C0就大工告成了，如果没有，请执行:

> sudo gedit /etc/default/grub

注释掉原来的三行（有两行是在（1）中添加的）

> GRUB_CMDLINE_LINUX_DEFAULT="quiet splash”
> GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_pstate=disable"
> GRUB_CMDLINE_LINUX_DEFAULT="processor.max_cstate=1 intel_idle.max_cstate=0 idle=poll”

把它们都写到一行去，用空格隔开：

> GRUB_CMDLINE_LINUX_DEFAULT="quiet splash quiet intel_pstate=disable processor.max_cstate=1 intel_idle.max_cstate=0 idle=poll"
>

然后更新并重启即可。

> sudo update-grub
> sudo reboot

### 安装配置

克隆源码

> sudo apt-get install git
> git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git

如果外网访问速度太差，见0x03.

配置eNB

> sudo gedit ~/openairinterface5g/targets/PROJECTS/GENERIC-LTE-EPC/CONF/enb.band7.tm1.usrpb210.conf

需要更改和确认的部分如下：前三行在MME中可以查到，之后就是把IP对应换成自己的EPC和eNB所在IP。

```shell
tracking_area_code  =  "1";
mobile_country_code =  "208";
mobile_network_code =  "92";


////////// MME parameters:
    mme_ip_address      = ( { ipv4       = "192.168.12.62";
                              ipv6       = "192:168:30::17";
                              active     = "yes";
                              preference = "ipv4";
                            }
                          );
    NETWORK_INTERFACES :
    {
        ENB_INTERFACE_NAME_FOR_S1_MME         = "eth0";
        ENB_IPV4_ADDRESS_FOR_S1_MME           = "192.168.12.82/24";
        ENB_INTERFACE_NAME_FOR_S1U            = "eth0";
        ENB_IPV4_ADDRESS_FOR_S1U              = "192.168.12.82/24";
        ENB_PORT_FOR_S1U                      = 2152; # Spec 2152
};
```


编译eNB

> cd openairinterface5g
> source oaienv
> cd cmake_targets
> sudo ./build_oai -I -w USRP

编译后无红色报错即可

运行eNB

> cd ~/openairinterface5g
> source oaienv
> cd cmake_targets
> ./build_oai --eNB -c -w USRP (这条运行一次就行了 确认安装)
> cd lte_build_oai/build
> sudo -E ./lte-softmodem -O $OPENAIR_DIR/targets/PROJECTS/GENERIC-LTE-EPC/CONF/enb.band7.tm1.usrpb210.conf -d

## 0x03 网络优化

建议安装上ubuntu之后就不要进行更换镜像源操作，然后全局走能连上外网的代理，并且在network处设置proxy，这样就能一劳永逸的解决后续下载速度问题:

>  http_proxy=’http://ip:port’ 
>
>  https_proxy=’http://ip:port’
>
>  socks_proxy='socks://ip:port'  