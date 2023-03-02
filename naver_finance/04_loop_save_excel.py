import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

def crawl(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"

    res = requests.get(url)

    # BeautifulSoup Html Parse
    bsobj = BeautifulSoup(res.text, "html.parser")

    div_today = bsobj.find("div", {"class": "today"})
    em = div_today.find("em")
    price = em.find("span", {"class": "blind"}).text  # 현재가격

    h_company = bsobj.find("div", {"class": "h_company"})
    name = h_company.a.text  # 회사명
    div_description = h_company.find("div", {"class": "description"})
    code = div_description.span.text  # 종목코드

    table_no_info = bsobj.find("table", {"class": "no_info"})
    td_s = table_no_info.tr.find_all("td")
    volume = td_s[2].find("span", {"class": "blind"}).text  # 거래량

    # 딕셔너리로 만들기
    dic = {"price": price,
           "name": name,
           "code": code,
           "volume": volume}
    return dic


codes = ["035720", "005930", "051910", "000660"]

r = []
for code in codes:
    dic = crawl(code)
    r.append(dic)

df = pd.DataFrame(r)
df.to_excel("prices.xlsx")