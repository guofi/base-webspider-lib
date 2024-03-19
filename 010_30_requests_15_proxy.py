import requests

"""
对于某些网站，在测试的时候请求几次，能正常获取内容。但是一旦开始大规模爬取，
对于大规模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，更甚者可能会直接封禁客户端的 IP，
导致一定时间段内无法访问。


"""

"""
pip3 install "requests[socks]"


"""


def fun():
    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }

    # proxies = {
    #     'http': 'socks5://user:password@host:port',
    #     'https': 'socks5://user:password@host:port'
    # }

    # proxies = {'https': 'http://user:password@10.10.1.10:3128/', }

    requests.get('https://www.taobao.com', proxies=proxies)


"""

"""
if __name__ == "__main__":
    fun()
