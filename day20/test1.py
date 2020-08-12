#web Crawling 
#긁어오는 것 crawling>>> 다량의 데이터를 긁어오는 것 
#여러 사이트를 정기적으로 여러 사이트를 정기적으로 돌며 정보를 추출하는 기술

#w3c --- WEB 표준을 정할 때 많이 등장하는 단체 https://www.w3.org/ 
#크롬, 사파리 웹의 표준을 수용하여, html 5>>> 수용, 표준으로 가자 
#video,audio태그 추가되면서  웹에서 video, audio 사용가능 (별도의 것 없이)
#  xml표준웹으로 밀어줄려고 많이 노력함.


#해외사이트와 국내 주식을 
##전세계사이트에서 긁어서 한 화면에 뿌림. 

#>>>> 우리회사 DB에 다 담음 


#web Scraping 
#웹사이트 특정 정보를 추출하는 기술을 scraping이라고 함. 


#웹 사이트 
#HTML CSS, JAVAscript 웹브라이징해서 보여줌, 받은 다음 보이게끔함 

import requests#서버 요청보님, 그 요청 처리하는 묘듈 


#pip install requests 

res = requests.get("http://google.com") #네이버 페이지 가서 페이지를 얻어 
print("응답코드:",res.status_code) #메인 서버 나에게 주고 


#404는 뭔가 이상한 상태 
#서버사이드 프로그램하다보면-->>>>500
# 403권한이 없을 때  

#<Response [200]> 200은 정상페이지 응답이야. 
#200: 정상(HTTP:status)
#404 : 페이지를 찾을 수 없음 : url 오류 
#url(uniform resource Location):#자원의 위치를 규격화시켜놓은것 
#500 : 서버 사이드 로직 에러 
#일반적 개발자가 무엇을 하거나 심각한 문제가 생겼을 때
# 
if res.status_code == requests.codes.ok: #200:뭔지 모를 수 있어 
    #requests.code가 200이란 소리, 상수로 만들어놓음  
    print("OKOKOK")
    #print(len(res.text))#응답받아온 것에 글자가 뭔지 찍어보기 

    #몇자인지 알고 싶어요 


res.raise_for_status()
#에러가 있으면 에러 메세지를 출력하고 바로 종료(시켜주는 함수)
# #에러 없으면 아래코드실행 


#저장하고 싶어요 
#print(res.text) #디스크에 저장하고 싶어요. 찍은 것을 
with open("google.html","w",encoding="utf-8") as f:
    f.write(res.text)  #기본 뼈대는 가져옴 