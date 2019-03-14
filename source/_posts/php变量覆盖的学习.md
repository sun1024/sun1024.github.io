---
title: php变量覆盖的学习
tags: php
---
# 关于php变量覆盖漏洞：
关注函数：extract(),parse_str(),$$,import_request_varables(),etc.

## extract():
栗子:
```php
<?php 
$a = 2333;
@extract($_GET);
print_r($a);
?>
```
payload:
`?a=1//即可覆盖$a`
## parse_str():
栗子:
```php
<?php
$a=2333;
parse_str($_SERVER['QUERY_STRING']);
print $a;
?>
```
payload:
`?a=1//即可覆盖$a`
## $$:
栗子:
```php
<?php 
$a = 2333;
foreach(array('_COOKIE','_POST','_GET') as $_request){
	foreach($$_request as $_key=>$_value){
		$$_key = addslashes($_value);
	}
}
print_r($a)
?>
```
payload:
`?a=1//即可覆盖$a`