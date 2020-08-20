#gb_70 : 로그인 버튼의 ID
#로그인 이메일 id: identifierId

from selenium import webdriver #selenium에서 webdriver를 불러옴. 

from selenium.webdriver.common.keys import Keys  #selenium.webdriver.common.keys에서 keys를 불러옴. 
import time  #time을 불러옴. 
import pyautogui #pyautogui를 불러옴.
import pyperclip #pyperclip을 불러옴. 

url = "http://www.naver.com" #url지정.  #http://www.naver.com을 url에 대입   
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe") #드라이버경로 못찾으면 경로 다 쓰세요 
browser.get(url) #browser을 대상으로 url을 가져옴. 


#PS E:\dev\python_workspace\day24> python pyauto3.py

#로그인 버튼 누르기 
elem = browser.find_element_by_class_name("link_login") #여기에   #
elem.click() #클릭하고 


# # time.sleep(1)
elem = browser.find_element_by_id("id")  #element의 id가 id인 애를 브라우져를 대상으로 
elem.send_keys("j69230") #페이지 다음 넘어가야 하는데 브라우저가 약간 느려지면 한번에 팍 쏴버리는데 브라우저 먹었는지 안 먹었는지 신경 안씀 너무 
# # elem.send_keys(Keys.ENTER)
# elem.send_keys("msuser") #아이디를 나눠서 써줌 
# elem.send_keys("9999991")
time.sleep(1)
elem = browser.find_element_by_id("pw")
elem.send_keys("gksksla09A@")  #패스워드
time.sleep(1)

# elem.send_keys("999999991")
# time.sleep(1)



browser.find_element_by_class_name("btn_global").click()  #로그인 버튼을 클릭 
#tab My_TAB_MAIL

time.sleep(2)  #2초 잠들게 함. 

pyautogui.alert("로그인 완료후 버튼을 클릭하세요.")  #이걸 만나면 멈춰있음   #창 뜨게 만듦 

#현재창을 크게 하자. 
browser.maximize_window()  

#메일쓰기 위치를 클릭 
pyautogui.click(1341,511) #여기를 클릭해줘   


#메일쓰기 위치를 클릭
#Point(x = 1339, y = 516)

pyautogui.click(1483,554)
# browser.find_element_by_css_selector(".tab.My_TAB_MAIL").click()  #java여서 확인이 안됨, 좌표값 같이 써줘야 함. 
# browser.find_element_by_css_selector(".func").click()
time.sleep(2)


#i프레임 >>>> 메일쓰기, 좌표쓰고 들어가야 함. 
pyautogui.click(481,343) #받는 사람 좌표 
pyautogui.write("j69230@naver.com")

pyautogui.click(440,419)  #제목 좌표 

pyperclip.copy("행운의 편지")   #카피하고 
pyautogui.hotkey("ctrl", "v") #ctrl+v해 
# pyautogui.write("use") #한글을 하려면 
# pyautogui.write("use")  #윈도우는 클립보드에 복사한 내용을 다른 데 복사넣기하는 것이 기본적으로 있음 


pyautogui.click(351,553)  #글 쓰는 데 좌표 
pyperclip.copy("이 편지는 영국에서 시작해서... 하루에 3통 안보내면 내가 싫어할거야.._")
# pyautogui.write("this is a mail. you can read this") #클립보드 사용안할 때 영어는 가능 
pyautogui.hotkey("ctrl", "v")
pyautogui.click(300,295)


# Point(x=481, y=343) 받는 사람 
# Point(x=430, y=417)#제목 
# Point(x=351, y=553)  글 쓰는 데 
#Point(x=300, y=295) 보내기 
#이미지 불러와 해도 됨 

#마우스 좌표 구하기 (cmd)
# C:\Users\user>e:

# E:\>cd dev

# E:\dev>cd python_workspace

# E:\dev\python_workspace>cd day24

# E:\dev\python_workspace\day24>python
# Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pyautogui
# >>> pyautogui.positon()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'pyautogui' has no attribute 'positon'
# >>> import pyautogui
# >>> pyautogui.position()
# Point(x=605, y=298)
# >>> pyautogui.position()
# Point(x=1341, y=511)



