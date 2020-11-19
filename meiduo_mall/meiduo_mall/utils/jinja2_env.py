from jinja2 import Environment
from django.urls import reverse
# 获取静态文件
from django.contrib.staticfiles.storage import staticfiles_storage

# jinja2环境
def jinja2_environment(**options):
    # 创建环境对象
    env = Environment(**options)
    # 自定义语法：{{static('静态文件相对路径')}} {{url('路由的命名空间')}}重定向
    # 全局配置 globals
    env.globals.update({
        # 'key':'value'
        # 获取静态文件的前缀
        'static':staticfiles_storage.url,
        # 使用的是url，但实际上是调用reverse()函数
        'url':reverse, # 重定向 == 反向解析
    })
    # 返回环境对象
    return env