"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/4/24 10:15
@Filename			: file_management.py
@Description		: 文件管理功能视图
@Software           : PyCharm
"""
from rest_framework.views import APIView

from language.LanguagePack import RET
from utils.customize_toolset import CstResponse
from utils.fastdfs.fdfs_storage import FastDFSStorage


class Test(APIView):

    def get(self, request):
        return CstResponse(RET.OK, data=request.query_params)


class FileUpload(APIView):
    """文件上传"""

    def post(self, request):
        file_obj = request.FILES.get("image")
        storage_obj = FastDFSStorage()
        file_id = storage_obj.save(file_obj.name, file_obj)
        url = storage_obj.url(file_id)
        return CstResponse(RET.OK, data=url)
