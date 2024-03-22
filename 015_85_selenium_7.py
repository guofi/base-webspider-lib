from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
显式等待

这里首先引入 WebDriverWait 这个对象，指定最长等待时间，然后调用它的 until() 方法，传入要等待条件 expected_conditions。
比如，这里传入了 presence_of_element_located 这个条件，代表节点出现的意思，其参数是节点的定位元组，也就是 ID 为 q 的节点搜索框
'''


def fun():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com/')
    wait = WebDriverWait(browser, 0.1)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)


'''
<selenium.webdriver.remote.webelement.WebElement (session="3404544cab4c89eeb29d92516a31af91", element="f.D9CF68EB78DFAB0371EA5BE3BF1DB05A.d.28F611A536C1B929F782C5208BDF2EC5.e.1")> 
<selenium.webdriver.remote.webelement.WebElement (session="3404544cab4c89eeb29d92516a31af91", element="f.D9CF68EB78DFAB0371EA5BE3BF1DB05A.d.28F611A536C1B929F782C5208BDF2EC5.e.22")>

'''
if __name__ == '__main__':
    fun()
