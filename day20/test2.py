import requests   #requests를 불러옴 

url = "https://search.naver.com/search.naver?query=날씨"    #url를 
res = requests.get(url)
res.raise_for_status() 
print(res.text)  #res의 text를 출력한다.(가져온다)

#브라우저내에서 바꿀수 있음 

#f12 개발자 도구 
#ctrl shift c 

#지정하고 내 이름 쓰기 
#밖에서는 볼 수 없음 
#어디밑에 어느 것 갖고와 할수 있으면 크롤링할수있는 것 
#html 기초구조알고 있어야 함. 