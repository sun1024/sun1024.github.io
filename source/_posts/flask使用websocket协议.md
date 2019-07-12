---
title: flask使用webSocket协议
date: 2019-7-12
tags: backend
---

# 0x01 前言

最近项目上需要实现后端的实时推送，而http作为一个单向的通信协议，必须一个request，一个response的进行，于是想到了webSocket ，webSocket 是 HTML5 开始提供的一种在单个 TCP 连接上进行全双工通讯的协议，可以很容易的实现Web的实时通信. 在这里谈一下自己在flask框架下使用webSocket的粗略实践.



# 0x02 flask-socketio简单使用

flask使用flask-socketio的扩展来实现webSocket.

安装方法:

>pip install flask-socketio

参考[官网](https://flask-socketio.readthedocs.io/en/latest/)写了一个后端推送的简单栗子：

服务器(app.py)：

```python
#!/usr/bin/python
# -*- coding : utf-8 -*-
# author : b1ng0

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
import time, json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('client_event')
def client_msg(msg):
    while 1:
        emit('server_response', {'data': msg['data']})
        time.sleep(2)

    
@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})

if __name__ == '__main__':
    socketio.run(
        app,
        debug=True,
        host='0.0.0.0',
        port=5000
        )
```

客户端(templates/index.html)：

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>Flask-SocketIO Test</title>
    <script type="text/javascript" src="//cdn.bootcss.com/jquery/3.1.1/jquery.min.js"></script>
    <script type="text/javascript" src="//cdn.bootcss.com/socket.io/1.5.1/socket.io.min.js"></script>
    <script type="text/javascript" charset="utf-8">
    $(document).ready(function() {
        var socket = io.connect();

        socket.on('connect', function() {
            socket.emit('connect_event', {data: 'connected!'});
            socket.emit('client_event', {data: 'test'});
        })

        socket.on('server_response', function(msg) {
            $('#log').append('<br>' + $('<div/>').text('Received #' + ': ' + msg.data).html());
        });

        $('form#emit').submit(function(event) {
                socket.emit('client_event', {data: $('#emit_data').val()});
                return false;
            });
    });
    
    </script>   
</head>
<body>
    <h2>WebSokect</h2>
    <div id='log'></div>
</body>
</html>
```

运行效果：(每隔2秒推送一次)

![](/images/1562856278162.png)



# 0x03 一些坑点

貌似实现了效果，但是在运行的时候，才发现原来使用的是"假的"webSocket:

![](/images/1562856476624.png)

提示信息如下：

> WebSocket transport not available. Install eventlet or gevent and gevent-websocket for improved performance.

查阅了一些资料，发现其实使用的是长轮询（polling) 的方式在运行，要使用真正的“ws://”还得安装一些异步服务，比如：eventlet/gevent/gevent-websocket，这里安装了eventlet：

> pip install eventlet

然而安装之后，客户端根本接收不到，连socketio.on函数都没有触发运行。再次一顿乱搜，发现都是前人踩过的坑了，原来是服务端陷入死循环，会影响与客户端之间的websocket连接。参考flask_socketio的示例程序，使用后台线程进行while循环解决了这个问题。

改进后的服务端：

```python
#!/usr/bin/python
# -*- coding : utf-8 -*-
# author : b1ng0

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from threading import Lock
import time, json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)
thread = None
thread_lock = Lock()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('client_event', namespace='/test_conn')
def client_msg(msg):
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

def background_thread():
    while 1:
        socketio.sleep(2)
        socketio.emit('server_response', {'data': 'test'}, namespace='/test_conn')

    
@socketio.on('connect_event', namespace='/test_conn')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
    socketio.run(
        app,
        debug=True,
        host='0.0.0.0',
        port=5000
        )
```

改进后的客户端：

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>Flask-SocketIO Test</title>
    <script type="text/javascript" src="//cdn.bootcss.com/jquery/3.1.1/jquery.min.js"></script>
    <script type="text/javascript" src="//cdn.bootcss.com/socket.io/1.5.1/socket.io.min.js"></script>
    <script type="text/javascript" charset="utf-8">
    $(document).ready(function() {
        // var socket = io.connect();
        namespace = '/test_conn';
        var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

        socket.on('connect', function() {
            socket.emit('connect_event', {data: 'connected!'});
            socket.emit('client_event', {data: 'test'});
        })

        socket.on('server_response', function(msg) {
            $('#log').append('<br>' + $('<div/>').text('Received #' + ': ' + msg.data).html());
        });

        $('form#emit').submit(function(event) {
                socket.emit('client_event', {data: $('#emit_data').val()});
                return false;
            });
    });
    
    </script>   
</head>
<body>
    <h2>WebSokect</h2>
    <div id='log'></div>
</body>
</html>
```



# 0x04 参考链接

https://flask-socketio.readthedocs.io/en/latest/

https://github.com/miguelgrinberg/Flask-SocketIO

https://www.cnblogs.com/luozx207/p/9714487.html

