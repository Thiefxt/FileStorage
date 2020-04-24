"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/4/24 10:15
@Filename			: file_management.py
@Description		: 
@Software           : PyCharm
"""
from rest_framework.views import APIView


class Test(APIView):

    def get(self, request, *args, **kwargs):
        return