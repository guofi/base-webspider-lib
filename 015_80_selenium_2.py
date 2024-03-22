from selenium import webdriver

'''
访问淘宝
'''


def fun():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    print(browser.page_source)
    browser.close()


if __name__ == '__main__':
    fun()
