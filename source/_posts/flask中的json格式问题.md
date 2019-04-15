---
title: flask中的json格式问题
date: 2019-4-10
tags: flask
---
最近尝试用flask框架写点api, 发现使用json或者jsonify都不能将decimal格式的数据转换为json格式。
解决方案：

```python
import  decimal

class DecimalEncoder(json.JSONEncoder):

　　def default(self, o):

　　　　if isinstance(o, decimal.Decimal):

　　　　　　return float(o)

　　　　super(DecimalEncoder, self).default(o)

# and then:

json.dumps(chart_list,..., cls=DecimalEncoder)

class JSONEncoder(json.JSONEncoder):
    
    def default(self, o):
        
        if isinstance(o,ObjectId):
            
            return str(o)
        
        if isinstance(o,Decimal):
            
            return str(o)
        
        return json.JSONEncoder.default(self,o)
    
配置到flask应用中

app.json_encoder = JSONEncoder
```
python做web真是麻烦, 还不如用世界上最好的语言curd一把梭(逃。。。
参考：[flask json 格式下 decimal 不是正确格式的问题](https://www.cnblogs.com/libaibuaidufu/p/10152233.html)

