# coding=utf-8
import urllib.request
import urllib.parse


def resp(json, url):
    """

    :param json:
    :param url:
    :return:
    """
    data = bytes(urllib.parse.urlencode(json), encoding='utf8')
    response = urllib.request.urlopen(url, data)
    """
{
	"args": {},
	"data": "",
	"files": {},
	"form": {
		"hello": "world"
	},
	"headers": {
		"Accept-Encoding": "identity",
		"Content-Length": "11",
		"Content-Type": "application/x-www-form-urlencoded",
		"Host": "httpbin.org",
		"User-Agent": "Python-urllib/3.9",
		"X-Amzn-Trace-Id": "Root=1-65f8f2ee-12ad75c26ebcbf773694d8e3"
	},
	"json": null,
	"origin": "119.123.41.143",
	"url": "http://httpbin.org/post"
}
    """
    print(response.read())


if __name__ == '__main__':
    json = {'hello': 'world'}
    url = 'http://httpbin.org/post'
    resp(json, url)
