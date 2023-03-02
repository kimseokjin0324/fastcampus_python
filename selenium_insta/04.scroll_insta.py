from selenium import webdriver
import chromedriver_autoinstaller
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.implicitly_wait(3)   #로딩할 시간을 기다리게 옵션을 줌 wait()이랑 비슷한듯

url ='https://www.instagram.com/'

driver.get(url =url)

#xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'

id =os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")

input_id =driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
input_id.send_keys(id) #id를 넘길수 있음

input_password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
input_password.send_keys(password)

#로그인 버튼 Xpath를 가져와서 클릭 동작까지해보기
##driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)
time.sleep(10)

# Search 기능 만들기
hashtag ="강아지"
url = f"https://www.instagram.com/explore/tags/{hashtag}"
driver.get(url =url)
time.sleep(6)
print(driver.page_source)

for _ in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  #해당 자바스크립트를 실행하겠다
    time.sleep(7)


time.sleep(10)


