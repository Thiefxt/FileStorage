"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/4/24 10:06
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path

from sf_file.views import file_management


urlpatterns = [
    path("test", file_management.Test.as_view()),                                                           # 测试运行

    path("upload", file_management.FileUpload.as_view()),                                                   # 文件上传
]
