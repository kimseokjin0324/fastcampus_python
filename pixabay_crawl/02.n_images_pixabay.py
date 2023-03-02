from time import sleep
from urllib.request import Request, urlopen

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# Pixabay URL에 접근


url = 'https://pixabay.com/ko/images/search/사과/?pagi=2'
driver.get(url=url)

# find(), find_all() .find_elements
image_area_xpath = '/html/body/div[1]/div[2]/div/div[3]/div/div[3]'
image_area = driver.find_element(By.XPATH, image_area_xpath)
image_elements = image_area.find_elements(By.TAG_NAME, 'img')

image_urls = []

for image_element in image_elements:
    image_url = ""
    if image_element.get_attribute("data-lazy") is None:
        image_url = image_element.get_attribute("src")
    else:
        image_url = image_element.get_attribute("data-lazy")
    image_urls.append(image_url)

# print("image_url", image_url)
#
for i in range(len(image_urls)):
    image_url =image_urls[i]
    # 이미지를 파일로 저장하기 (byte형태로)
    image_byte = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
    f = open(f'apple{i}.jpg', 'wb')  # wb =byte형태로 write하겠다.
    f.write(urlopen(image_byte).read())
    f.close()

sleep(30)
