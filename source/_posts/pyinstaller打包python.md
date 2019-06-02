---
title: pyinstaller打包python
date: 2019-6-2
tags: python
---
# 0x00 前言



迫于某"科研项目"的奇葩要求，需要将python代码打包为exe，网上找了有不少解决方案（py2exe、PyInstaller、cx_Freeze，etc.），这里尝试了下pyinstaller，用着还算顺手。

# 0x01 安装：



>  pip install pyinstaller

# 0x02 打包命令：



> pyinstaller app.py -F -i app.ico -p C:/python/Lib/site-packages

# 0x03 常用参数：



| 参数                    | 用法                                                         |
| ----------------------- | ------------------------------------------------------------ |
| -F, –onefile            | 打包一个单个文件，如果你的代码都写在一个.py文件的话，可以用这个，如果是多个.py文件就别用 |
| -D, –onedir             | 打包多个文件，在dist中生成很多依赖文件，适合以框架形式编写工具代码，我个人比较推荐这样，代码易于维护 |
| -K, –tk                 | 在部署时包含 TCL/TK                                          |
| -a, –ascii              | 不包含编码.在支持Unicode的python版本上默认包含所有的编码.    |
| -d, –debug              | 产生debug版本的可执行文件                                    |
| -w,–windowed,–noconsole | 使用Windows子系统执行.当程序启动的时候不会打开命令行(只对Windows有效) |
| -c,–nowindowed,–console | 使用控制台子系统执行(默认)(只对Windows有效)                  |
| -s,–strip               | 可执行文件和共享库将run through strip.注意Cygwin的strip往往使普通的win32 Dll无法使用. |
| -X, –upx                | 如果有UPX安装(执行Configure.py时检测),会压缩执行文件(Windows系统中的DLL也会) |
| -o DIR, –out=DIR        | 指定spec文件的生成目录,如果没有指定,而且当前目录是PyInstaller的根目录,会自动创建一个用于输出(spec和生成的可执行文件)的目录.如果没有指定,而当前目录不是PyInstaller的根目录,则会输出到当前的目录下. |
| -p DIR, –path=DIR       | 设置导入路径(和使用PYTHONPATH效果相似).可以用路径分割符(Windows使用分号,Linux使用冒号)分割,指定多个目录.也可以使用多个-p参数来设置多个导入路径，让pyinstaller自己去找程序需要的资源. |
| –icon=<FILE.ICO>        | 将file.ico添加为可执行文件的资源(只对Windows系统有效)，改变程序的图标  pyinstaller -i  ico路径 xxxxx.py |
| –icon=<FILE.EXE,N>      | 将file.exe的第n个图标添加为可执行文件的资源(只对Windows系统有效) |
| -v FILE, –version=FILE  | 将verfile作为可执行文件的版本资源(只对Windows系统有效)       |
| -n NAME, –name=NAME     | 可选的项目(产生的spec的)名字.如果省略,第一个脚本的主文件名将作为spec的名字 |



# 0x04 参考

<https://pyinstaller.readthedocs.io/en/v3.3.1/usage.html>

<https://blog.csdn.net/BearStarX/article/details/81054134>

