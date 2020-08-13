# 외부의 데이터 가져올 거예요. 
import requests 
from bs4 import BeautifulSoup as bs  #여기 패기지로 부터 패키지 가져오고 별칭 줌 
from pprint import pprint #보기좋게 출력하고 싶어요. 
#원본 문서자체는 \t 있었는데 브라우저는 \t 무시함.

url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853"

#요청하는 것을 reque get 가져오는 것. get 주소창에서 가져오는 것 


res = requests.get(url) #응답 가져옴 
#아 주소로 get방식으로 url요청합니다. 

#200정상죈 


# print(res)
# #상태 코드 번호 가지고 있음 

# print(res.status_code) #res의 status-code를 불러와 
# print(res.text)  

#데이터 보기 좋게 가져오려면

res.raise_for_status()
# 별도의 라이브러리 있으면 편함 
res.close() #하면 자원반납해야함. 안 그러면 계속 놀고 있음. 
#pip install bs4 설치 
#프로그램에 끌어다 쓸 수있음 
# pprint(res.text) #아까보다 보기 좋게 출력 
soup=bs(res.text,"lxml") #이 문서를 해석하자, 해석기 lxml이 성능좋음 이 글자를 이 해석기로 해석해줘  
#res에 있는 text를 lxml로 해석해줘 bs는 Beauigulsoup의 별칭임. 
print(soup) #soup를 출력 
#이상한 문자들 정리됨
# print(soup,type(soup))
# class 면 인스턴스 함수랑 변수 들어있어요. 
#print(soup.title) #soup에서 title이란 애를 찾아줘. 
#타이틀 태그가 아니라 내용이 필요 
print(soup.title.get_text()) #글자만 갖고 올 수 있음 
print("------------------------------------------")
print(soup.find("a")) #soup 객체에서 처음 발견되는 a element 출력
#현지 페이지 내에서 움직이은 링크 # >> #menu
print("--------------------------------------------------------")
print(soup.a.attrs) #a앨리먼트의 속성들을 볼 수 있음 
#a태그에 속성들
# {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}
# PS E:\dev\python_workspace> 
# 하이퍼래퍼런스 속성만 갖고 오고 싶어요
print("---------------------------------------------------")
print(soup.a.attrs['href']) #soup을 이용 

# 함수를 이용한 접근(도 가능)
print(soup.find("td",attrs={"class","title"})) #찍어본 것  
#분석한 페이지 뷰티플 숲 객체 에서 찾아라 td라는 태그 중에서 속성 attrs 클래스인 애로 그 값이 title 
#속성이 타이틀인 애를 찾아줘 
#클래스가 타이틀인 애만 얻고 싶습니다. 
#td에서 클래스가 타이들인 애만 얻고 싶어/ 
print("------------------------------------------------------------")
title1=soup.find("td",attrs={"class","title"})

a = title1.find("a") #거기에서 다시 a태그를 찾아와 #위의 속성은 항상 줘야하는 것이 아니라 주면 구체적인 것 
#안 줘도 됨 
print(a) #출력 
print(a.get_text()) #get text로 갖고 오면 됨 



#제목 전부를 얻고 