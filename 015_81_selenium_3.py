from selenium import webdriver
from selenium.webdriver.common.by import By

'''
访问淘宝
'''


def fun():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input_first = browser.find_element(By.ID, 'q')
    input_second = browser.find_element(By.CSS_SELECTOR, '#q')
    input_third = browser.find_element(By.XPATH, '//*[@id="q"]')
    print(input_first, input_second, input_third)
    browser.close()


'''
<selenium.webdriver.remote.webelement.WebElement (session="7a9a9a5afa2cf8da4078cf2891028e35", element="f.023DD2B3E8E93AACDC53FE157574CB04.d.135063371A89FF0D0F429D3D93BD3838.e.1")> 
<selenium.webdriver.remote.webelement.WebElement (session="7a9a9a5afa2cf8da4078cf2891028e35", element="f.023DD2B3E8E93AACDC53FE157574CB04.d.135063371A89FF0D0F429D3D93BD3838.e.1")>
<selenium.webdriver.remote.webelement.WebElement (session="7a9a9a5afa2cf8da4078cf2891028e35", element="f.023DD2B3E8E93AACDC53FE157574CB04.d.135063371A89FF0D0F429D3D93BD3838.e.1")>

'''
if __name__ == '__main__':
    fun()
