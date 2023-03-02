# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import requests

url = "https://openapi.naver.com/v1/search/blog.json?query=교대역 맛집&start=101&display=100"
res =requests.get(url,headers={"X-Naver-Client-Id":"LbN1zSrSHN0PLtdAOGIS",
                               "X-Naver-Client-Secret":"qciFEpGUt2"})

r = res.json()
print(len(r['items'])) # default값이 10개임 naver api는
for item in r['items']:
    print(item)
