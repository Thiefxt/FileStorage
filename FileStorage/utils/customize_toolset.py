"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/4/24 10:17
@Filename			: customize_toolset.py
@Description		: 
@Software           : PyCharm
"""

import logging

from rest_framework.response import Response
from language.LanguagePack import Language


logger = logging.getLogger(__name__)


class CstResponse(Response):

    def __init__(self, code, message=None, data=None, **kwargs):
        """
        自定义返回数据
        :param data: 返回数据
        :param code: 返回状态码
        :param message: 返回消息
        """
        if not message:
            message = Language.get(code)

        dic_data = dict(
            code=int(code),
            msg=message
        )
        if data:
            dic_data['data'] = data
        else:
            dic_data['data'] = None
        super(CstResponse, self).__init__(dic_data, **kwargs)


class CstException(Exception):
    """
    业务异常类
    """
    def __init__(self, code, message=None):
        self.code = code
        self.message = message
        super(CstException, self).__init__(message)