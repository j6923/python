#자바 스크립트로 데이터를 가져오려고요. 
from selenium import webdriver #selenium에서 webdriver을 가져와 

from selenium.webdriver.common.keys import Keys  #selenium.webdriver.common.keys에서 keys가져와 

import time #time을 불러와 
import pyautogui #pyautogui을 불러와 

url = "http://www.naver.com"  #url에 "http://www.naver.com"를 대입.   

browser=webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe") #어디서든 실행할 수 있게 경로 지정함. 
#브러우저 열고 네이버로 
browser.get(url) #browser을 대상으로 url을 가져옴. 

#현재창을 크게 
browser.maximize_window()
#검색: query

elem = browser.find_element_by_id("query")  #browser을 대상으로 element의 id를 찾는다 query로 

elem.click()  #elem을 클릭한다. 

time.sleep(3) #3초 잠잔다. 
elem.send_keys("종로3가맛집")  #elem를 대상으로 키를 보내는데 "종로3가맛집"키를 보낸다. 
elem.send_keys(Keys.ENTER)    #elem을 대상으로 엔터키를 치는 Keys.ENTER으로 enter키를 친다. 


#아래로 스크롤
pyautogui.scroll(-1500) # 아래로 -1000만큼 스크롤 

#제목을 얻어옴 
for i in range(1,21):
    ulELem = browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul") 
    #print(ulELem)
    lists = ulELem.find_elements_by_css_selector(".list_item.type_restaurant") #클래스 명이니까 .들어감. css선택잨슬 때 .으로 지칭 동시에 클래스 #CSS에서 .클래스는 .이어서 클래스 2개 들어가 있음.  #클래스는 동시에 여러개 줄 수 있음. css...spss써도 됨. 
    for store in lists:    
        print(store.find_element_by_css_selector("div.tit > span > a > span").text) #한 애의 글자를 가져와  #앞의 것만 써서 전체 맛집 크롤링
        #print("--------------------------------------------------------------") #한개씩 뜰때마다 "----------------"출력 

    pyautogui.click(765,580)  #x좌표 765, y좌표 599클릭하게 함. 
    print("-------------------------------------------------")  #"------------------"을 출력 
    #time.sleep(3) #a.json으로 가져와 시간 지연됨 
    #자바스크립트 웹페이지두고 네이버 데이터 보이지 않고 웹브 a젝스로 작동해서 그냥 접근 안됨, 클릭이 되어야만 갱신이 됨,,, 좌표값으로 

    print("------------------------------------------------------------------------------------------------------")

#여기까지 가게목록가져옴. 
# ulELem = browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul") 
# #print(ulELem)
# lists = ulELem.find_elements_by_css_selector(".list_item.type_restaurant") #클래스 명이니까 .들어감. css선택잨슬 때 .으로 지칭 동시에 클래스 
# #정확하게 지칭하는 것 알아낼 수 있음 

# #for 문 해서 하면 모든것 디비에 insert해서 다 집어넣을 수있음. 디비데이터까지 할수 있음. 

#링크에 store number가 있음 
#a 반복문돌면서 브라우저 get한다음 시간 전화번호 주소 가져와서 db에 넣는다든가 네이버 가져오면서 db insert하면 다량의 데이터 넣을 수 있을 거예요. 



#같은 값이면 self. 함수명 
