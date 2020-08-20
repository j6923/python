# 외부의 데이터 가져올 거예요. 
import requests 

url = "http://www.naver.com"  #"http://www.naver.com"을 url에 대입해라. 

#요청하는 것을 reque get 가져오는 것. get 주소창에서 가져오는 것 

res = requests.get(url)  #url로 get방식으로 요청합니다. 
#아 주소로 get방식으로 url요청합니다. 

#200정상값  


# print(res)
# #상태 코드 번호 가지고 있음 

# print(res.status_code) #res의 status-code를 불러와 
# print(res.text)  

#데이터 보기 좋게 가져오려면

res.raise_for_status()
# 별도의 라이브러리 있으면 편함 

#pip install bs4 설치 
