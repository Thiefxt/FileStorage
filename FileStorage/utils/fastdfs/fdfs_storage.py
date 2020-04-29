"""
@Author				: Thief
@Email				: 18773993654@163.com
@Lost modifid		: 20-4-23 23:04
@Filename			: fdfs_storage.py
@Description		: 
@Software           : PyCharm
"""
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings


class FastDFSStorage(Storage):
    """自定义文件存储系统类"""

    def __init__(self, base_url=None, client_conf=None):
        """自定义初始化方法"""

        self.base_url = base_url or settings.FDFS_BASE_URL
        self.client_conf = client_conf or settings.FDFS_CLIENT_CONF

    def _open(self, name, mode='rb'):
        """
        存储系统打文件存储的文件时调用此方法,因为我们自定义文件存储系统类,
        :param name: 打文件的文件名
        :param mode: 打开文件的模式  read bytes
        :return: None
        """
        pass

    def _save(self, name, content):
        """
        上传文件时会调用此方法,让文件上传到远程FastDFS服务器中
        :param name: 要上传的文件名
        :param content: 要上传的文件对象 将来需要content.read() 文件二进制读取出并上传
        :return: file_id
        """
        # 创建fastDFS客户端对象 指定客户端配置文件
        client = Fdfs_client(self.client_conf)
        # 上传文件
        ret = client.upload_by_buffer(content.read())  # 如果要上传的是文件数据二进制数据流,可以用此方法上传文件,并且上传后,此文件没有后缀

        # 判断文件是否上传成功
        if ret.get('Status') != 'Upload successed.':
            raise Exception('Upload file failed')

        file_id = ret.get('Remote file_id')  # 获取字典中的file_id
        return file_id

    def exists(self, name):
        """
        每次进行上传文件之前就会先调用此方法进行判断,当前要上传的文件是否已经在stroage服务器
        :param name: 要进行判断是否上传的那个文件名
        :return: True(文件已存在,不上传了) / False(文件不存在,可以上传)
        """
        return False

    def url(self, name):
        """

        :param name: 要下载的文件file_id
        :return: Storage服务器ip:端口 + file_id
        """
        return self.base_url + name
