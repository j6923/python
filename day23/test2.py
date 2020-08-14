#만약 클래스의 이름을 모른다면 상태가 조금 어렵다면 
#웹 브라우저의 자동화를 가능하게 하는 다양한 도구와 라이브러리 포함하는 프로젝트 >>>>>>>>>>>> selenium 이라고 함. 
#마우스 클릭 하는 작업을 눈으로 보면서 시킬 수 있음. 


#webdriver 필요
#브라우저 버전 확인 필요함. 

#구글 주소창에 edge://version/


#버전 : 84.0.4147.125 
#크롬드라이버 --- 구글에 맨 첫번째애 

#압축풀어서 workspace에 복사 
#pip install selenium 해주기 

from selenium import webdriver  #함수를 불러옴 

from selenium.webdriver.common.keys import Keys
import time 

#크롬 드라이버 객체를 생성 
browser = webdriver.Chrome("e:/dev/chromedriver.exe")  #실행할 작업이 여기에 있어서 따로 ("c:..~~..?") 경로지정해줘야함.  #webdriver을 chrome으로 생성하고 browser에 대입, 그래서 browser이라는 객체 생성 
#brower을 웹 브라우저 객체라고 생각하면 됨  #"e:/DEV/""
#이 주소에 get방식으로 연결해 
#id가 query여서 ,, query라는 엘리먼트로 쿼리 찾아 
#브라우저 객체로 네이버 웹페이지 접속 
browser.get("http:www.naver.com")  #웹 브라우저 강제로 뜨게 함. 


#검색창 엘리먼트 객체 
#이 브라우저에게 앨리번트 찾을 건데 앨리먼트 이름이 아이디가 쿼리 이 앨리먼트 객체 가져옴
element = browser.find_element_by_id("query") #브라우저에서 앨리먼트를 찾을 건데 id(이름)이 query인 것을 찾아서 element에 대입.
time.sleep(3) 
element.click() #창을 띄우면서 클릭함 #앨리먼트를 클릭해줘. 클릭이라는 함수 호출 

#글자를 쓰려면  
element.send_keys("택배 없는 날 ") #엘리먼트로 "택배 없는 날"로 키를 보내라
#로그인으로 자동적으로 할 수 있음. #매크로라고 함. 
#일반 피시에서도 가능 

#C:WUsersWuser>ping 127.0.0.1 -t 
#W는 원가표시 
#오류나면 명령 프롤프트에서 쓰기 .
#터미널에서 pip uninstall 하면 삭제됨. 
element.send_keys(Keys.ENTER) #엔터 티값 key.enter  #브라우저 페이지 로딩되어야 하는데 정말 후룻 쳐버려서 확인했으니까 에러는 안내고 느리거나 그러면 대기시켜야함 
# browser.close() # 브라우저 클로즈해. 



#3초 후에 구글로 이동 
time.sleep(3)
browser.get("http://www.google.com")



#name q라고 되어있음 class도 있지만 더 짧음 
element = browser.find_element_by_name("q") #엘리먼트로 찾아, name tag이름으로 찾을래 class로 찾을래  #엄밀히 말하면 search element 
#엘리먼트를 클릭 
element.click()
#검색키워드를 입력 
element.send_Keys("광복절")
element.send_Keys(Keys.ENTER) #엔터 
time.sleep(3) #3초 기다림 
element.send_Keys(Keys.BACKSPACE)
element.send_Keys(Keys.BACKSPACE)
element.send_Keys(Keys.BACKSPACE)
element.send_keys("독립기념일 ㅠ.ㅠ") 
element.send_Keys("휴일")
element.send_Keys(Keys.ENTER)




