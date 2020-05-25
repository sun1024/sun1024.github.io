---

title: vps搭建CobaltStrike
date: 2020-5-25 18:09
tags: CobaltStrike
---

## 0x01 前言

手贱重装了下服务器，各种线上环境都没了，在这里记录一下cs的搭建，免得每次都像个憨憨到处找。。。



## 0x02 服务端搭建

```bash
// 1. CobaltStrike破解版下载
// 来自ssooking师傅的破解：https://www.cnblogs.com/ssooking/p/12535998.html
$ git clone https://gitee.com/ssooking/cobaltstrike-cracked.git

// 2. vps上安装java环境 ubuntu环境
// JDK官网下载还要注册 亲测使用openJDK也完全可以
$ apt install openjdk-8-jre-headless
// 测试
$ java -version
openjdk version "1.8.0_252"
OpenJDK Runtime Environment (build 1.8.0_252-8u252-b09-1~18.04-b09)
OpenJDK 64-Bit Server VM (build 25.252-b09, mixed mode)

// 3. 解压cobaltstrike4.0-cracked 运行teamserver即可
$ ./teamserver 公网ip password
[*] Will use existing X509 certificate and keystore (for SSL)
[+] Team server is up on *****
[*] SHA256 hash of SSL cert is: ************************************************

// 个人习惯nohup长期运行
$ nohup ./teamserver 公网ip password &
```



## 0x03 客户端连接

客户端也是用上面的cobaltstrike4.0-cracked文件夹，安装好java环境后双击start.bat即可：

![](/images/image-20200525112443061.png)

按服务端配置填写connect:

![](/images/image-20200525112950735.png)



## 0x04 CS简单加固

- 修改默认端口

  ```
  // 默认端口50050 在teamserver中改掉即可
  $ vim teamserver
  // 最后一行 50050 改成放行的端口
  # start the team server.
  java -XX:ParallelGCThreads=4 -Dcobaltstrike.server_port=50050 -Djavax.net.ssl.keyStore=./cobaltstrike.store -Djavax.net.ssl.keyStorePassword=123456 -server -XX:+AggressiveHeap -XX:+UseParallelGC -classpath ./cobaltstrike.jar server.TeamServer $*
  ```

- 修改证书信息

  ```
  // 可以重新生成一次 但是太麻烦 不如直接改掉CobaltStrike特征 又不是拿来干坏事(笑
  $ vim teamserver
  // keytool部分 在改端口的前两行
  keytool -keystore ./cobaltstrike.store -storepass 123456 -keypass 123456 -genkey -keyalg RSA -alias cobaltstrike -dname "CN=Major Cobalt Strike, OU=AdvancedPenTesting, O=cobaltstrike, L=Somewhere, S=Cyberspace, C=Earth"
  //瞎改下
  keytool -keystore ./cobaltstrike.store -storepass 123456 -keypass 123456 -genkey -keyalg RSA -alias cobaltstrike -dname "CN=abc, OU=abc, O=abc, L=abc, S=abc, C=abc"
  ```

  

## 参考

https://www.cnblogs.com/ssooking/p/12535998.html

https://www.3hack.com/note/96.html