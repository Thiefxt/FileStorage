"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/4/24 10:15
@Filename			: file_management.py
@Description		: 
@Software           : PyCharm
"""
from rest_framework.generics import GenericAPIView

from language.LanguagePack import RET
from utils.customize_toolset import CstResponse


class Test(GenericAPIView):

    def get(self, request):
        return CstResponse(RET.OK, data=request.query_params)
