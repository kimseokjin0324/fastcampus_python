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

def login (id,password):
    input_id =driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_id.send_keys(id) #id를 넘길수 있음

    input_password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    input_password.send_keys(password)

    #로그인 버튼 Xpath를 가져와서 클릭 동작까지해보기
    ##driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()
    driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)


def search(hashtag, scroll_times):
    url = f"https://www.instagram.com/explore/tags/{hashtag}"
    driver.get(url =url)
    time.sleep(6)
    print(driver.page_source)

    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  #해당 자바스크립트를 실행하겠다
        time.sleep(5)

def like_comment(nth,comment,repeat):
    # 몇번째(nth) 포스트 클릭 하는 지
    row = (nth-1) // 3 + 1
    col = (nth-1) % 3 + 1
    xpath =f'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{row}]/div[{col}]'

    driver.find_element(By.XPATH,xpath).click()

    for _ in range(repeat):
        # like
        like_xpath ='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button'
        driver.find_element(By.XPATH,like_xpath).click()

        time.sleep(5)
        #comment
        comment_xpath ='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea'
        driver.find_element(By.XPATH, comment_xpath).click()
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)

        #게시버튼 누르기
        comment_button_xpath ='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]/div'
        driver.find_element(By.XPATH,comment_button_xpath).click()

        #다음버튼누르기
        next_button_xpath ='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/button'
        driver.find_element(By.XPATH, next_button_xpath).click()

id =os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")

login(id,password)

time.sleep(10)

# Search 기능 만들기
hashtag ="강아지"
search(hashtag,0)

like_comment(15,"강아지가 귀엽네요",2)

time.sleep(10)


