from selenium import webdriver

PATH = '/Users/zabi/Google Chrome for Testing.app'


driver = webdriver.Chrome(PATH)

driver.get('google.com')