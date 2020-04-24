"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/4/24 10:18
@Filename			: LanguagePack.py
@Description		: 
@Software           : PyCharm
"""
class RET:
    """
    语言类包
    """
    OK = "200"
    DBERR = "501"
    NODATA = "462"
    DATAEXIST = "433"
    DATAERR = "499"
    REQERR = "521"
    IPERR = "422"
    THIRDERR = "431"
    IOERR = "502"
    SERVERERR = "500"
    UNKNOWERR = "451"
    USER_STATUS = "465"


# 元组中第一个为中文，第二个为英文，第三个为繁体
language_pack = {
    RET.OK: ("成功",),
    RET.DBERR: ("数据库查询错误",),
    RET.NODATA: ("数据不存在",),
    RET.DATAEXIST: ("数据已存在",),
    RET.DATAERR: ("数据格式错误",),
    RET.REQERR: ("非法请求或请求次数受限",),
    RET.IPERR: ("IP受限",),
    RET.THIRDERR: ("第三方系统错误",),
    RET.IOERR: ("文件读写错误",),
    RET.SERVERERR: ("内部错误",),
    RET.UNKNOWERR: ("未知错误",),
    RET.USER_STATUS: ("账号已被禁用，如有疑义请联系平台客服",),
}


class Language(object):

    _lang ='zh_cn'

    @classmethod
    def init(cls, lang):
        cls._lang = lang

    @classmethod
    def get(cls, value):
        lang = language_pack.get(value)
        if not lang:
            return None
        if cls._lang == 'zh_cn' and len(lang) > 0:
            return lang[0]
        elif cls._lang == 'en_US' and len(lang) > 1:
            return lang[1]
        elif cls._lang == 'zh_F' and len(lang) > 2:
            return lang[2]






