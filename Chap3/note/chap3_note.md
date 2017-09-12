本文记录使用 Flask 快速完成一个 简易天气查询 MVP 程序的探索，学习过程。程序采用Flask+Jinja2实现，其中Flask扩展包括：1、flask-bootstrap，2、Flask-WTF。前端使用 jQuery Ajax 提交 Post，jQuery DOM 操作实现局部刷新显示 JSON 数据。实时天气数据使用心知天气 API 获取。

## 需求
* 完成一个**网页版天气查询程序**
  * 实现以下功能：
    * 基本功能
      * 输入城市名，获取该城市最新天气情况
      * 点击「帮助」，获取帮助信息
      * 点击「历史」，获取历史查询信息
    * 部署在命令行界面

## 实现
### 搭建开发环境
假定已安装Python3.5；pip3和virtualenv，这里所说的开发环境搭建指本程序所需的依赖包安装。使用virtualenv创建虚拟环境，默认情况下，虚拟环境会依赖系统环境中的site packages，就是说系统中已经安装好的第三方package也会安装在虚拟环境中，所发请加上``` --no-site-packages ``` 参数，表示不包括系统全局的Python安装包，这样会令环境更干净。在虚拟环境执行如下语句：
```
pip install flask
pip install Flask-WTF
pip install flask-bootstrap
```
首先安装 flask Python web 框架，然后安装 Flask-WTF 表单扩展，最后是安装 flask-bootstrap 集成 Twitter Bootstrap 前端框架。

### 项目文件结构
```
project <-- 根目录
   ├─static  <-- 存放静态文件
   │  ├─css
   │  ├─img
   │  └─js
   └─templates <-- 存放模板文件
   ```
   考虑到这是一个简单的 Web 应用，而没有按照 Flask 大型应用的方式组织项目文件结构，这里主要是构建了放置静态文件和模板文件的目录，方便管理前端文件。

### 代码实现
* 编写业务逻辑

  本应用的核心业务是通过 API 获取实时天气数据，作为一个练习的应用，会考虑免费的天气 API ，考虑到网络问题，也倾向于选择国内的 API 服务。综上，这里选择心知天气API提供实时数据。心知天气 API 提供 Python Demo ，返回 JSON 格式数据。根据需求，我们对返回数据进行重新组装，如果数据复杂的话还需要创建为实体对象保存，传递。业务类保存为 weather_servers.py 文件。

* 编写 Flask 路由

  需求中的三个功能点只有获取该城市最新天气情况和获取历史查询信息是动态数，帮助作为静态信息是无需向服务器请求的。所以这里只需要编写两个路由。保存在 weather_app.py 文件中。为了提升用户体验，另外还加了一个错误处理的路由，找不到资源时返回 404 页面。

* 编写 Flask-WTF 表单

  搭建网页时，如果需要和用户交互，就会用到表单。使用 Flask-WTF 能简化我们的工作。如字段验证，使用宏渲染大量字段等。本应用由于表单并不复杂，只用到了字段验证功能。保存在 WeatherForm.py 文件中。

* 编写前端

    前端中 Html 部分主要包含主页面 index.html ，404 页面的 404.html ，‘_data’后缀的 Html 文件是显  示动态数据的模板。主页面初始时显示帮助信息，当点击不同按钮采用 jQuery DOM 操作隐藏，显示相应  的数据。主页页通过 继承 Bootstrap 基础页面使用 Flask-Bootstrap 模板。  
    ![使用 Flask-Bootstrap 模板](https://raw.githubusercontent.com/JeetChan/LearnPythontheHardWay/master/image/Chap3_html.jpg)  
    因为需要引入 其他 JS 和 CSS 文件，使用了Jinja2 提供的super() 函数。  如：
   ```
   {{ super() }}
   <link rel="stylesheet" href="https://bootswatch.com/cerulean/bootstrap.min.css">
   ```
     这里引用了 bootswatch 主题样式。

## 程序发布
  Python项目中必须包含一个 requirements.txt 文件，用于记录所有依赖包及其精确的版本号。以便新环境部署。运行如下命令生成  requirements.txt 文件：  
    ``` pip freeze >requirements.txt ```  
      当需要创建这个虚拟环境的完全副本，可以创建一个新的虚拟环境，并在其上运行以下命令：  
     ``` pip install -r requirements.txt ```

## 效果图

![页页初始状态（帮助）](https://raw.githubusercontent.com/JeetChan/LearnPythontheHardWay/master/image/Chap3_help.jpg)  
![天气查询](https://raw.githubusercontent.com/JeetChan/LearnPythontheHardWay/master/image/Chap3_search.jpg)  
![历史信息](https://raw.githubusercontent.com/JeetChan/LearnPythontheHardWay/master/image/Chap3_history.jpg)  

## 代码
  代码托管在 [GitHub](https://github.com/JeetChan/LearnPythontheHardWay/tree/master/extended/Chap3/project) 中，安装 requirements.txt 文件指定的依赖库，进入 weather_app.py 文件所在的目录，运行 ``` piython weather_app.py ``` 命令即可部署。
## 参考

  [思诚之道博客，Flask系列文章](http://www.bjhee.com/tag/flask)

# CHANGELOG
* 170903 添加效果图
* 170901 创建
