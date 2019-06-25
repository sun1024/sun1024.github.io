---
title: flask-mail使用qq邮箱
date: 2019-6-25
tags: backend
---

# 0x00 前言

最近在看狗书，准备系统性的学习一下flask，但是在<<电子邮件>>那章作者使用了gmail作为邮箱服务，笔者配了很久都发不出去，可能是天朝特色导致不能使用gmail的，于是探索了一下flask框架下使用qq邮箱发送电子邮件。



# 0x01 qq邮箱配置

因为是使用SMTP服务发送电子邮件，所以首先要去qq邮箱设置页开启：

![1561425672893](C:\Users\User\AppData\Roaming\Typora\typora-user-images\1561425672893.png)

开启后会得到一个授权码作为邮箱密码使用



# 0x02 flask配置

- 先贴一个flask-mail的配置项

| 配置项                     | 默认值      | 功能                                                         |
| -------------------------- | ----------- | ------------------------------------------------------------ |
| **MAIL_SERVER**            | localhost   | 邮箱服务器                                                   |
| **MAIL_PORT**              | 25          | 端口                                                         |
| **MAIL_USE_TLS**           | False       | 是否使用TLS                                                  |
| **MAIL_USE_SSL**           | False       | 是否使用SSL                                                  |
| **MAIL_DEBUG**             | app.debug   | 是否为DEBUG模式，打印调试消息                                |
| **MAIL_SUPPRESS_SEND**     | app.testing | 设置是否真的发送邮件，True不发送                             |
| **MAIL_USERNAME**          | None        | 用户名，填邮箱                                               |
| **MAIL_PASSWORD**          | None        | 密码，填授权码                                               |
| **MAIL_DEFAULT_SENDER**    | None        | 默认发送者，填邮箱                                           |
| **MAIL_MAX_EMAILS**        | None        | 一次连接中的发送邮件的上限                                   |
| **MAIL_ASCII_ATTACHMENTS** | False       | 如果 MAIL_ASCII_ATTACHMENTS 设置成 True 的话，文件名将会转换成 ASCII 的。一般用于添加附件。 |

- 安装flask-mail:

> pip **install** Flask-Mail

- 配置config  (这里的配置与书中gmail配置稍有不同)：

```python
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_qq@qq.com'
app.config['MAIL_PASSWORD'] = 授权码
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'your_qq@qq.com'
app.config['FLASKY_ADMIN'] = 'your_qq@qq.com'
```

send_mail  (抄自狗书)：

```python
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
```



# 0x03 发送成功

![1561426625808](C:\Users\User\AppData\Roaming\Typora\typora-user-images\1561426625808.png)



# 0x04 参考链接

[Flask 文档](https://dormousehole.readthedocs.io/)

[Flask Web开发：基于Python的Web应用开发实战（第2版）](https://item.jd.com/32399773056.html)

[flask-email手册](https://pythonhosted.org/Flask-Mail/)

[使用 Flask-Mail 和 qq 邮箱 SMTP 服务发送邮件](https://juejin.im/entry/594266e35c497d006bc4ae22)