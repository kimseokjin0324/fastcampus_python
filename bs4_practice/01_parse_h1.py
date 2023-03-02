from bs4 import BeautifulSoup
# bs4란 HTML또는 XML구조에서 필요한 값만 뽑아주는 체

bsobj = BeautifulSoup("<html><body><h1>안녕하세요</h1></body></html>", "html.parser")
print(bsobj)

# .find() .find_all()은 두개 다름

#1. find("안에 태그이름이 들어감"): 태그를 찾는거임
h1= bsobj.find("h1")
print(h1)
print(h1.text)