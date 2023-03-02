from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.implicitly_wait(3)   #로딩할 시간을 기다리게 옵션을 줌 wait()이랑 비슷한듯

url ='https://www.instagram.com/'

driver.get(url =url)

xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
