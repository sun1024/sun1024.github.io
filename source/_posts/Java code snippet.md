---
title: Java code snippet
date: 2020-2-19
tags: java
---

> 在家里就各种拖延症，不想看论文，不想挖洞，只能强迫自己刷刷题假装在学习的样子，在这里整理一下java常用的数据结构，记不住了就过来copy。。。

## Array & ArrayList

```java
int[][] myArr = new int[5][10];
ArrayList<String> myArr = new ArrayList<String>();
myArr.add("dynamically resizing");
System.out.println(myArr.get(0));
```

## Vector

```java
Vector<String> myVect = new Vector<String>();
myVect.add("synchronized");
System.out.println(myVect.get(0));
```

## LinkedList

```java
LinkedList<String> myList = new LinkedList<String>();
myList.add("build-in list");
Iterator<String> iter = myList.iterator();
while (iter.hasNext())
System.out.println(iter.next());
```

## HashMap

```java
HashMap<String,String> map = new HashMap<String,String>();
map.put("key","value");
System.out.println(map.get("key"));
```

## Stacks

```java
Stack<Object> stack = new Stack<Object>();
Object push(Object element)
Object pop()
Object peek()
Object isEmpty()
```

## Queues

```java
Queue<Object> queue = new LinkedList<Object>();
Object offer()
Object poll()
boolean isEmpty()
```

## Dictionaries

```java
private static Dictionary<Object, Object> dic = new Hashtable<Object, Object>();
Object put(Object key, Object value)
Object get(Object key)
Enumeration elements()
Enumeration keys()
Object remove(Object key)
boolean isEmpty()
boolean contains(Object key)
int size()
```

## StringBuilder

```java
StringBuilder string = new StringBuilder();
StringBuilder append(char c)
StringBuilder deleteCharAt(int index)
int length()
```

## Strings

```java
char charAt(int index)
int indexOf(char ch)
String concat(String s)
String substring(int beginIndex)
String substring(int beginIndex, int endIndex)
String toLowerCase()
String toUpperCase()
boolean contains(CharSequence s)
static String copyValueOf(char[] data)
char[] toCharArray()
int length()
boolean contenEquals(StringBuffer sb)
boolean startsWith(String prefix)
boolean endsWith(String suffix)
boolean matches(String regex)
String intern()
String trim()
```

## Math

```java
xxx abs(xxx x)
double ceil(double d) 
double ceil(float f)
double floor(double d)
double floor(float f)
double int(double d)
long round(double d)
int round(float f)
double exp(double d)
double log(double d)
double pow(double base, double exponent)
Double E, PI
```

