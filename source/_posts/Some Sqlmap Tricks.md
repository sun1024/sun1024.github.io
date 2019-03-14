---
title: Some Sqlmap Tricks
tags: Sqlmap
---
## 0x01 --prefix,--suffix
在注入的payload的前面或者后面加一些字符, 使sql语句能正常拼接:

`--prefix "xxx" --suffix "xxx"`

## 0x02 --start --stop
表中的数据量过多, 或者盲注太费时间, 使用--start,--stop指定几行数据:

`--start num1 --stop num2`

## 0x03 --search 
寻找特定的数据库名，所有数据库中的特定表名，所有数据库表中的特定字段:

`--search -C sfzh`

## 0x04 --count
只获取表中的数据个数:

`--count -D testDB`

## 0x05 一些tamper

如果web应用使用asp/asp.net开发，charunicodeencode.py和percentage.py可以绕过Waf。

`--tamepr=charunicodeencode`
`--tamepr=percentage`

## 参考

[sqlmap用户手册](http://119.29.64.123:8080/WooyunDrops/#!/drops/25.sqlmap%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C)
[如何使用SQLMap绕过WAF](http://www.freebuf.com/articles/1000.html)