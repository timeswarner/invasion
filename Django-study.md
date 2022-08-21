# 18.1 建立项目

## 18.1.2建立虚拟环境
Python -m venv ll_env

## 18.1.2激活虚拟环境
ll_env\scripts\activate

## 18.14安装Django
Pip install django

## 18.1.5在Django中创建项目
Django-admin startproject learning_log .

* setting.py指定Django如何与系统交互以及如何管理项目，在开发项目过程中，我们将修改其中一些设置，并添加一些设置。
* 文件ulrs.py告诉Django应创建哪些页面来响应浏览器请求。
* 文件wsgi.py帮助Django提供它创建的文件，这个文件就是web服务器网关接口


## 18.1.6 创建数据库
python manage.py migrate

## 18.1.7查看项目
python manage.py runserver

# 18.2 创建应用程序
python manage.py startapp learning_logs 

## 18.2.1 定义模型
用models.py来定义应用程序中管理的数据

## 18.2.2 激活模型
* 定义模型：修改models.py，
* 激活模型：如果是第一次定义模型，需要注册。迁移模型：对learning_logs调用makemigrations，
* 修改数据库：Django迁移项目，python manage.py migrate

## 18.2.3 Django管理网站
1. 创建超级用户:python mange.py createsuperuser
2. 向管理网站注册模型:admin.site.register(Topic)
3. 添加主题:
   
# 18.3 创建页面
1. 定义url
2. 编写视图
3. 编写模板
   ## 18.3.1 定义url
   