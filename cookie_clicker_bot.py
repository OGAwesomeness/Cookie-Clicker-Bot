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
        
        upgrades(page)
        you(page, cookies)
        cortext_baker(page, cookies)
        idleverse(page, cookies)
        javascript_console(page, cookies)
        chancemaker(page, cookies)
        chancemaker(page, cookies)
        prism(page, cookies)
        anti_condenser(page, cookies)
        time_machine(page, cookies)
        portal(page, cookies)
        alchemy(page, cookies)
        shipment(page, cookies)
        wizard_tower(page, cookies)
        temple(page, cookies)
        bank(page, cookies)
        factory(page, cookies)
        mine(page, cookies)
        farm(page, cookies)
        grandma(page, cookies)
        cursor(page, cookies)
    
    
def cursor(page, cookies):
    price = page.find_element(By.XPATH, '//*[@id="productPrice0"]')
    product = page.find_element(By.XPATH, '//*[@id="product0"]').get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product0"]').click()


def grandma(page, cookies):
    price = page.find_element(By.XPATH, '//*[@id="productPrice1"]')
    product = page.find_element(By.XPATH, '//*[@id="product1"]').get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product1"]').click()
        
        
def farm(page, cookies):
    price = page.find_element(By.XPATH, "//*[@id='productPrice2']")
    product = page.find_element(By.XPATH, '//*[@id="product2"]').get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product2"]').click()
        
        
def mine(page, cookies):
    price = page.find_element(By.XPATH, "//*[@id='productPrice3']")
    product = page.find_element(By.XPATH, '//*[@id="product3"]').get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product3"]').click()
        
        
def factory(page, cookies):
    price = page.find_element(By.XPATH, "//*[@id='productPrice4']")
    product = page.find_element(By.XPATH, "//*[@id='product4']").get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product4"]').click()
        
        
def bank(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice5']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product5"]').click()
        
        
def temple(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice6']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product6"]').click()
        
        
def wizard_tower(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice7']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product7"]').click()
        
        
def shipment(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice8']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product8"]').click()
        
        
def alchemy(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice9']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product9"]').click()
        
        
def portal(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice10']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product10"]').click()
        
        
def time_machine(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice11']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product11"]').click()
        
        
def anti_condenser(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice12']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product12"]').click()
        
        
def prism(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice13']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product13"]').click()
        
        
def chancemaker(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice14']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product14"]').click()
        
        
def javascript_console(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice15']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product15"]').click()
        
        
def idleverse(page, cookies):
    price = int(page.find_element(By.XPATH, "//*[@id='productPrice16']").text)
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product16"]').click()
        
        
def cortext_baker(page, cookies):
    price = page.find_element(By.XPATH, "//*[@id='productPrice17']")
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product17"]').click()
        
        
def you(page, cookies):
    price = page.find_element(By.XPATH, "//*[@id='productPrice18']")
    product = price.get_attribute('class')
    if product == 'product unlocked enabled':
        if int(cookies[0].replace(',','')) >= int(price.text.replace(',', '')) or price.text in ' '.join(cookies):
            page.find_element(By.XPATH, '//*[@id="product18"]').click()


def upgrades():
    pass
    
    
main()