import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

'''
切换子页面
'''


def fun():
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    try:
        logo = browser.find_element(By.CLASS_NAME, 'logo')
    except NoSuchElementException:
        print('NO LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element(By.CLASS_NAME, 'logo')
    print(logo)
    print(logo.text)


'''
NO LOGO
<selenium.webdriver.remote.webelement.WebElement (session="5a545ec78f8185e2a9374b08c42790b7", element="f.B07F560AD60FE6A17ACB92409EBD4097.d.F1A1A4679D037E9B04FCBA629F1517DD.e.25")>

'''
if __name__ == '__main__':
    fun()
