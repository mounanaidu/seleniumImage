from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def get_screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)
    driver.get(url)
    time.sleep(5)
    element = driver.find_element_by_xpath('//*[@id="root"]')
    width = 1500
    height = element.size['height']
    driver.set_window_size(width,height)
    time.sleep(2)
    element.screenshot("screenshot.jpg")
    driver.quit()

get_screenshot("http://google.com")