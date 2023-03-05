import requests

url = 'https://www.ev.or.kr/portal/localInfo'
data = requests.get(url)
print(data.text)

#매번할때 호출하면 데이터가 많은경우 너무 느릴수도 있음 -> 호출 후 데이터를 file로 저장
f =open("local_info.html","w+",encoding="utf-8")
f.write(data.text)
f.close()