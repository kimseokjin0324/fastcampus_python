# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import requests

def call_api(keyword,start,count):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={count}"
    res =requests.get(url,headers={"X-Naver-Client-Id":"LbN1zSrSHN0PLtdAOGIS",
                                   "X-Naver-Client-Secret":"qciFEpGUt2"})

    print(res)
    r = res.json()
    # print(len(r['items'])) # default값이 10개임 naver api는
    # # for item in r['items']:
    # #     print(item)
    return r




if __name__ =='__main__':
    r = call_api("스트리머 랄로",101,100)
    for item in r['items']:
        print(item)