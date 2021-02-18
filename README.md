# 痒痒鼠鼠标点击辅助脚本

------

## 起源​ :kick_scooter:

灯姐的绘卷肝到我自闭，突发奇想能不能搞个脚本自己刷:hamburger:

于是乎说干就干我就搞起来了，我还是一个小菜鸡，然后的话希望大佬们能多给我几个勾协，超鬼王带我蹭个分，要是觉得好用的话请小灰喝杯咖啡hhh，冲冲冲！:rocket:

目前还在开发ing嘤嘤嘤:pensive:

------

## 如何开始 :beginner:

### 我只想使用​ ​ :ok_hand:

1.[点击我](https://github.com/lyhlyhl/yys_mouse_click/releases)下载最新版本yystool.zip

2.解压后，右击**以管理员身份运行**yystool.exe

3.开肝吧，大老鼠！

#### 我是开发者​ :pencil2:

##### tip:需要以管理员身份运行程序，以pycharm为例，右击以管理员身份打开pycharm

##### 命令行则需要右键执行命令行（否则会出现鼠标点击失效的现象）

![截图1](img/docs/截图1.png)

0. ### 需要环境：

   python3.6+

1. ### 配置环境:

   ```powershell
   #配置运行环境
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

2. 运行程序

   ```powershell
   python main.py
   ```

   或者是通过IDE直接运行main.py文件（比较推荐该方法）

------

## 开发记录​ ​ :pencil:

2020/12/4 目前已经完成了双人御魂，比较稳定。

2020/12/8 其实尝试接着写完这个界面，但是pyqt总觉得很怪，准备下一步用C++重构，可能目前打算是更新完当前的御灵，帮助大家刷绘卷吧。

2021/2/6 说是重构，但是由于考试和电脑坏了一直没开始，看了一些pyqt大佬开发的产品，感觉还是可以冲，主要是python需要解决的是环境问题，如果使用pyinstall打包的话就会很大:broken_heart:，好在需要安装的包也不算很多，准备弄个requirement，就可以完事了:hand:，然后继续这里开始开发，但是内部写的有点像一坨屎，准备改一改啥的。

2021/2/6 成功打包了文件，发布了第一版双开御魂可以使用版，很开心​ :smile:

2021/2/18 想拯救一下我那屎山代码，可是为什么有这么多玄学问题 :cry:

