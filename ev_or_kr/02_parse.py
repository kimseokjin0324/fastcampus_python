from bs4 import BeautifulSoup

f = open("local_info.html", encoding="utf-8")
page_string = f.read()

bsobj = BeautifulSoup(page_string,"html.parser")

# 웹 사이트 상 표만 가져오기
table = bsobj.find("table",{"class": "table_02_2_1"})

# 테이블 아래 tbody(우리가 필요한 데이터)
trs = table.find("tbody").find_all("tr")
tr = trs[0]

ths = tr.find_all("th")
tds = tr.find_all("td")

## 시도 뽑기
sido = ths[0].text
## 시군구 뽑기
region = ths[1].text

#민간 공고 대수 뽑아내기
민간공고대수 = tds[2]
#접수대수
접수대수 = tds[3]
#출고대수
출고대수 = tds[4]
#출고잔여대수
출고잔여대수 = tds[5]
print(민간공고대수)
print(접수대수)
print(출고대수)
print(출고잔여대수)
