from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def main():
    chromePath = 'C:\Windows\WinSxS\x86_netfx4-browser_files_b03f5f7f11d50a3a_4.0.15912.0_none_06d55e201f3d4256\chrome.browser'
    broserDriver = Service(chromePath)
    page = webdriver.Chrome(service=broserDriver)

    page.get('https://orteil.dashnet.org/cookieclicker/')
    time.sleep(2)
    page.find_element(By.XPATH, '//*[@id="langSelect-EN"]').click()
    time.sleep(2)

    action = webdriver.ActionChains(page)
    store = page.find_element(By.XPATH, '//*[@id="store"]')
    action.move_to_element(store)
    store.click()
    action.key_down(Keys.SPACE)
    action.perform()
    
    while True:
        page.find_element(By.XPATH, '//*[@id="bigCookie"]').click()
        cookies = (page.find_element(By.ID, 'cookies').text).split(' ')
        
        grandma(page, cookies)
        cursor(page, cookies)
    
    
def cursor(page, cookies):
    price = int(page.find_element(By.XPATH, '//*[@id="productPrice0"]').text)
    if int(cookies[0]) >= price:
        page.find_element(By.XPATH, '//*[@id="product0"]').click()


def grandma(page, cookies):
    price = int(page.find_element(By.XPATH, '//*[@id="productPrice1"]').text)
    if int(cookies[0]) >= price:
        page.find_element(By.XPATH, '//*[@id="product1"]').click()
    
    
main()