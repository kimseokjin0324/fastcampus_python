from bs4 import BeautifulSoup

f = open("local_info.html", encoding="utf-8")
page_string = f.read()

bsobj = BeautifulSoup(page_string, "html.parser")

# 웹 사이트 상 표만 가져오기
table = bsobj.find("table", {"class": "table_02_2_1"})

# 테이블 아래 tbody(우리가 필요한 데이터)
trs = table.find("tbody").find_all("tr")
tr = trs[0]

ths = tr.find_all("th")
tds = tr.find_all("td")

## 시도 뽑기
sido = ths[0].text
## 시군구 뽑기
region = ths[1].text

replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[
                             1:]  # 람다를 이용해서 괄호 여닫이 다 없애기 split을 해서 리스트를 반환시키기
form = lambda a, b, c, d, e: {"sido": a, "region": b, "sep1": c, "sep2": d, "value": e}

# 민간 공고 대수 뽑아내기
민간공고대수 = replace_brackets(tds[2].text)
# 접수대수
접수대수 = replace_brackets(tds[3].text)
# 출고대수
출고대수 = replace_brackets(tds[4].text)
# 출고잔여대수
출고잔여대수 = replace_brackets(tds[5].text)

print(민간공고대수)
##print(접수대수)
##print(출고대수)
##print(출고잔여대수)

l = [
    form(sido,region,"민간공고대수","우선순위",int(민간공고대수[0]))
]
print(l)
