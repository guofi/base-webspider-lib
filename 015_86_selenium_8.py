from selenium import webdriver

'''
Cookies
'''


def fun():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())


'''
[{'domain': '.zhihu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1711093766'}, {'domain': '.zhihu.com', 'expiry': 1745653764, 'httpOnly': False, 'name': 'd_c0', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ALCcVl9cWRiPTuU4SJ-gdffChXtsX3LHAYE=|1711093764'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': '_xsrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '77bf04b4-4443-41e7-b12f-0ac793ef677b'}, {'domain': '.zhihu.com', 'expiry': 1742629765, 'httpOnly': False, 'name': 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1711093766'}, {'domain': 'www.zhihu.com', 'httpOnly': False, 'name': 'KLBRSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '031b5396d5ab406499e2ac6fe1bb1a43|1711093766|1711093764'}, {'domain': '.zhihu.com', 'expiry': 1745653764, 'httpOnly': False, 'name': '_zap', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '2f499ae3-9920-4aae-9086-3078acccf223'}]
[{'domain': '.zhihu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1711093766'}, {'domain': '.zhihu.com', 'expiry': 1745653764, 'httpOnly': False, 'name': 'd_c0', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ALCcVl9cWRiPTuU4SJ-gdffChXtsX3LHAYE=|1711093764'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': '_xsrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '77bf04b4-4443-41e7-b12f-0ac793ef677b'}, {'domain': '.zhihu.com', 'expiry': 1742629765, 'httpOnly': False, 'name': 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1711093766'}, {'domain': '.www.zhihu.com', 'httpOnly': False, 'name': 'name', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'germey'}, {'domain': 'www.zhihu.com', 'httpOnly': False, 'name': 'KLBRSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '031b5396d5ab406499e2ac6fe1bb1a43|1711093766|1711093764'}, {'domain': '.zhihu.com', 'expiry': 1745653764, 'httpOnly': False, 'name': '_zap', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '2f499ae3-9920-4aae-9086-3078acccf223'}]
[]
'''
if __name__ == '__main__':
    fun()
