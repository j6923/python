# 외부의 데이터 가져올 거예요. 
import requests 
from bs4 import BeautifulSoup as bs  #여기 패기지로 부터 패키지 가져오고 별칭 줌 
from pprint import pprint #보기좋게 출력하고 싶어요. 
#원본 문서자체는 \t 있었는데 브라우저는 \t 무시함.

url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853"

#요청하는 것을 reque get 가져오는 것. get 주소창에서 가져오는 것 


res = requests.get(url) #응답 가져옴   requests에서 url을 
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

#클래스가 타이틀인 애만 얻고 싶습니다. 
#td에서 클래스가 타이들인 애만 얻고 싶어/ 
print("------------------------------------------------------------")
title1=soup.find("td",attrs={"class","title"})

a = title1.find("a") #거기에서 다시 a태그를 찾아와 #위의 속성은 항상 줘야하는 것이 아니라 주면 구체적인 것 
#안 줘도 됨 
print(a) #출력 
print(a.get_text()) #get text로 갖고 오면 됨 



#제목 전부를 얻고 
#이런 애들 다 찾아줘. 
tdList = soup.find_all("td", attrs={"class","title"})  #class와 title이 있는 것을 다 찾아줘 
#.get써도 되지만 ()해도 됨. 
print(tdList,type(tdList))
print("--------------------------------------------------")
print(tdList[0].find("a").get_text())
#0대신 1 , 1대신 2 하면 됨, 그래서 반복문 쓰면 됨 
for td in tdList:
    print(td.find("a").get_text())


#클래스는 여러개 발견한 첫번째 find고 find_all 다 찾아주는 것 \


#https://image-comic.pstatic.net/webtoon/20853/1237/20200727181900_61f49987b02fcaf216c2c03b617461fa_IMAG01_1.jpg
#을 복사해서 오른쪽 마우스 클릭 여러번 하면 시간 오래 걸림 여러사진은 