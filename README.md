# 花城智慧公交 WebApplication

Github: https://github.com/nutcore-net/PZH-BusService

Gitee: https://gitee.com/dtsdao/PZH-BusService/

## 简介

> 受 [chainsx](https://github.com/chainsx) 所托写的工具，感谢他提供的API

遵循 GPL v3.0 协议公开源码

使用海信提供给攀枝花公交公司的API来获取公交实时到站信息

主体程序为HTML文件，Python 脚本充当一个代理服务器提供API的访问权限，避免跨域问题

使用 [MDUI](https://www.mdui.org/) v0.4.2 作为前端库，遵守 Material Design 设计规范

## 使用说明

1. 首先需要有一台正在运行的服务器
   
   环境要求安装 Python 3.4 及以上

   需要互联网连接

2. 使用 Git clone本项目到服务器的某个地方
   
   或者你也可以下载release里的压缩HTML后的压缩包，然后自行解压

3. 更改 `server.py` 中 `conf` 的相关值
   
   - `servAddr` 为远端API地址
   - `pubAddr` 为你想绑定的本地地址
   - `bindPort` 为你想绑定的端口

4. 使用 Python 运行 `server.py` 启动代理服务器

5. 打开浏览器访问你设置的 `pubAddr`  就可以看到HTML页面

## 注意事项

1. 推荐通过nginx进行优化，如果想用https必须配置nginx
   
   方法为nginx代理到python脚本监听的端口就可以，网上有教程

2. 域名需要提前解析到本机ip，不然会报错
3. 如果想关掉终端也可以运行，Linux 可以使用 `nohup` 或 `screen`，Windows 大概远程桌面不关掉会话就行