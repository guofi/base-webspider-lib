import requests
import logging
from requests.packages import urllib3

"""
requests 还提供了证书验证的功能。当发送 HTTP 请求的时候，它会检查 SSL 证书，我们可以使用 verify 参数控制是否检查此证书

"""

"""
设置忽略警告的方式 或者 捕获警告到日志的方式忽略警告

我们也可以指定一个本地证书用作客户端证书，这可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组

本地私有证书的 key 必须是解密状态，加密状态的 key 是不支持的
"""


def fun():
    urllib3.disable_warnings()
    # logging.captureWarnings(True)
    response = requests.get('https://www.12306.cn', verify=False)

    # response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))

    print(response.status_code)


"""

"""
if __name__ == "__main__":
    fun()
