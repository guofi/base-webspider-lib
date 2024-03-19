# coding=utf-8
import urllib.request


def urlopen(url):
    response = urllib.request.urlopen(url)
    """
    <class 'http.client.HTTPResponse'>
    """
    # print(type(response))
    """
    200
    """
    # print(response.status)
    """
    [('Accept-Ranges', 'bytes'), ('Cache-Control', 'no-cache'), ('Content-Length', '227'), 
    ('Content-Security-Policy', "frame-ancestors 'self' https://chat.baidu.com http://mirror-chat.baidu.com https://fj-chat.baidu.com https://hba-chat.baidu.com https://hbe-chat.baidu.com https://njjs-chat.baidu.com https://nj-chat.baidu.com https://hna-chat.baidu.com https://hnb-chat.baidu.com http://debug.baidu-int.com;"), 
    ('Content-Type', 'text/html'), ('Date', 'Tue, 19 Mar 2024 01:50:23 GMT'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'),
     ('Pragma', 'no-cache'), ('Server', 'BWS/1.1'), ('Set-Cookie', 'BD_NOT_HTTPS=1; path=/; Max-Age=300'),
      ('Set-Cookie', 'BIDUPSID=0F31CC499FFE083198F3F1B98A2A8096; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'),
       ('Set-Cookie', 'PSTM=1710813023; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), 
       ('Set-Cookie', 'BAIDUID=0F31CC499FFE083128673C25CA3B02FC:FG=1; max-age=31536000; expires=Wed, 19-Mar-25 01:50:23 GMT; domain=.baidu.com; path=/; version=1; comment=bd'),
        ('Traceid', '171081302302388674669719776552971102997'), ('X-Ua-Compatible', 'IE=Edge,chrome=1'), ('X-Xss-Protection', '1;mode=block'), ('Connection', 'close')]
    """
    # print(response.getheaders())
    """
    BWS/1.1
    """
    print(response.getheader('Server'))
    # print(response.read().decode('utf-8'))


if __name__ == '__main__':
    urlopen('https://www.baidu.com')
