# coding=utf-8
import urllib.request


def fun():
    request = urllib.request.Request(url='https://python.org')
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    fun()
