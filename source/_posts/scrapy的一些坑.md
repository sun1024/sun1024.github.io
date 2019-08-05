---
title: scrapy的一些坑
date: 2019-8-5
tags: 爬虫 scrapy
---
## 导出数据时中文乱码

使用scrapy抓取的数据中含有中文时，因为中文默认是Unicode, 在使用-o参数导出时，无法显示。

解决方法：在setting.py中添加一行

```python
FEED_EXPORT_ENCODING = 'utf-8'
```

## meta参数的浅拷贝问题

多级爬取数据时，需要在多个页面中获取数据，使用meta参数可以在多个parse中传递值，但是由于meta是浅拷贝，当item中的数据需要重复爬取时，下一个函数接收item= response.meta['item']并不会及时更新，所以需要进行深拷贝：

```python
import copy

yield scrapy.Request(post_url, callback=self.parse_post_url,
                meta={'item':copy.deepcopy(item)})
```

## 参考链接

https://www.aisun.org/2017/10/python+scrapy/

https://www.zhihu.com/question/54773510/answer/146971644