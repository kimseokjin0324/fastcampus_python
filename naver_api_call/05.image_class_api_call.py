# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import requests
from urllib.request import Request, urlopen


class NaverSearchApi():
    api_url = "https://openapi.naver.com/v1/search/blog.json"

    def call_api(self, keyword, start=1, count=10):
        url = f"{self.api_url}?query={keyword}&start={start}&display={count}"
        res = requests.get(url, headers={"X-Naver-Client-Id": "LbN1zSrSHN0PLtdAOGIS",
                                         "X-Naver-Client-Secret": "qciFEpGUt2"})

        print(res)
        r = res.json()
        # print(len(r['items'])) # default값이 10개임 naver api는
        # # for item in r['items']:
        # #     print(item)
        return r

    def blog(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.get_paging_call(keyword, quantity)

    def news(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.get_paging_call(keyword, quantity)

    def webkr(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/webkr.json"
        return self.get_paging_call(keyword, quantity)

    def image(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/image"
        return self.get_paging_call(keyword, quantity)

    def save_images(self, r):
        image_url = r[0]['link']
        image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        f = open('0.jpg', 'wb')
        f.write(urlopen(image_byte).read())
        f.close()

    def get_paging_call(self, keyword, quantity):
        if quantity > 1100:
            # quantity =1100
            exit("ERROR 최대 요청할수 있는 건수는 1100건입니다.")

        repeat = quantity // 100
        display = 100

        if quantity < 100:
            display = quantity
            repeat = 1
        result = []
        for i in range(repeat):
            print(f"{i + 1}번 반복합니다")
            start = i * 100 + 1
            if start > 1000:
                start = 1000
            print(start)
            r = self.call_api(keyword, start=start, count=display)
            print(r['items'][0])
            result += r['items']
        return result


if __name__ == '__main__':
    naver_search_api = NaverSearchApi()
    r = naver_search_api.image("비트코인", 20)
    print(r)
    naver_search_api.save_images(r)
