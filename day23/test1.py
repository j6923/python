import requests  #리퀘스트를 불러옴. 
from bs4 import BeautifulSoup as bs #bs4에서 BeautifulSoup을 가져오고 bs라고 별칭 줌. 

from pprint import pprint  #pprint에서 pprint를 불러옴. 

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8" #주소를 가져옴. 

res = requests.get(url)   #url을 요청함. 

#print(res.text,len(res.text)) #몇 단어인지 찍어봄. 

#만약 에러있었다면 끝내고 없으면 하위코드 실행
#에러가 발생한다면 에러 메세지 출력후 종료 아니라면 하위에 코드를 실행
res.raise_for_status()   

pprint(res.text)      

#깔끔하게 하기위 해 
soup = bs(res.text,'lxml') #Beatiful #bs에서 res #이게.... 

dds = soup.find_all("dd", attrs={"class", "lvl"})   #soup에서 다 찾아 dd라는 태그를 lvl의 그런 속성을 가진 애를 
#규칙있는애가 lvl 
#dd라는 태그                    #SOUP의 값을 FIND해서 찾아오면 됨. 
#pprint(dds)

for d in dds: #d에서 자손인 클래스 값이  num 인 것을 가지고 오고 싶습니다,  그런 앨리먼트 선택한 다음 값 가져오면 됨. 
    print(d)
    num = d.find("span",attrs={"class", num}) #attrs의 목록으로는 클래스가 num  num의 그런 속성을 가진 태그 스판을 가져옴. 
    print("-----------------------------------------------------")
    print(num.get_text())  #num의 text를 가져옴
    print("------------------------------------------------")
#정의 목록 만들기 
#<dl> 정의 목록(defiition List)
    #<dt> 용어 제목 </dt> (definition term)신조 용어 단어는 이런 뜻입니다하고 태그를 달 때 쓰는 태그, 
    #<dd> 용어 설명 </dd> (definition description) dd는 용어에 대한 설명 
    #<
# div : 화면 왼쪽부터 오른쪽까지 다 차지 

#content의 공간만 찾이 하는  것 span 






#강수량을 크롤링 
temp = soup.find("span",attrs={"class", "todaytemp"}) #첫번때 것 가져옴. 
pprint(temp)
print(temp.get_text())

print("-------------------------------------------------------------------")
rainfall = soup.find("span",attrs={"class", "rainfall"})  #강수량 

pprint(rainfall)


#미세먼지  크롤링 
num2 = rainfall.find("span",attrs ={"class", "num"})
# print(num2)
print(num2.get_text())
print("==================================================================")#미세먼지