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

def get_paging_call(keyword,quantity):
    if quantity > 1100 :
        #quantity =1100
        exit("ERROR 최대 요청할수 있는 건수는 1100건입니다.")

    repeat = quantity//100
    result = []
    for i in range(repeat):
        print(f"{i+1}번 반복합니다")
        start = i*100+1
        if start > 1000:
            start =1000
        print(start)
        r = call_api(keyword,start=start,count = 100)
        print(r['items'][0])
        result +=  r['items']
    return result

if __name__ =='__main__':
    r = get_paging_call("스트리머 랄로",1100)
