#gb_70 : 로그인 버튼의 ID
#로그인 이메일 id: identifierId

from selenium import webdriver #selenium에서 webdriver 함수를 가져와 

from selenium.webdriver.common.keys import Keys #selenium.webdriver.common.keys에서 keys를 가져와 
import time #time을 불러와 
import pyautogui #pyautogui를 불러와 


url = "http://www.moakt.com/ko/mail" #http://www.moakt.com/ko/mail에서 가져옴. 경로를 지정 . url에 http://www.moakt.com/ko/mail대입 
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe") #드라이버경로 못찾으면 경로 다 쓰세요 

browser.get(url) #url을 가져옴. 


#PS E:\dev\python_workspace\day24> python pyauto3.py

#로그인 버튼 누르기 
elem = browser.find_element_by_class_name("mail_in") #여기에 
elem.click() #클릭하고 
elem.send_keys("j6923dsfffffjslffffjflsjflsdfffffdfsdfjfslkfjj") #이렇게 타자를 쳐 

# time.sleep(1)  #1초 잠을 잠. 
# elem = browser.find_element_by_id("identifierId")
# elem.click()
# elem.send_keys("j69230@naver.com") #페이지 다음 넘어가야 하는데 브라우저가 약간 느려지면 한번에 팍 쏴버리는데 브라우저 먹었는지 안 먹었는지 신경 안씀 너무 
# elem.send_keys(Keys.ENTER)


#임시메일 한 시간짜리만 받을 수 있는 이메일이 있음. 
#https://www.moakt.com/  : 대표회사 중 하나 

elem = browser.find_element_by_class_name("mail_butt")  #메일버튼을 
elem.click() #클릭 

time.sleep(2)  #2초 동안 잠을 잠. 

browser.find_element_by_class_name("iconic_button").click()#CLASS의 NAME이 iconic_button에 해당하는 것을 클릭 
#iconic_buttoon


time.sleep(2)


#browser.find_element_by_class_name("iconic_button").click()  #이거에 해당하는 것을 클릭 
#iconic_buttoon

 
time.sleep(2) #2초 잠을잠. 
elem = browser.find_element_by_name("mail_to")  #브라우저에서 이름이 mail_to인 앨리먼트를 찾고 elem에 대입해. 
elem.send_keys("dagda@hanafos.com")   #elem에 key를 보내 dagda@hanafos.com로, 보내는 사람을 씀 

elem = browser.find_element_by_name("mail_subject") #browser에 이름이 mail_subject인 이름을 가진애를 찾고 elem에 대입해 
elem.send_keys("자동 발송 메일 테스트 입니다")  #elem를 대상으로  자동 발송 메일 테스트 입니다라는 키를 보내. 

elem = browser.find_element_by_name("mail_text") #browser에 이름이 mail_text인 element를 찾고 elem에 대입해. 
elem.send_keys("자동 발송 메일 테스트 입니다. 호호호 삭제하세요 ^^ ") #elem에 자동 발송 메일 테스트 입니다. 호호호 삭제하세요 ^^ 라는 key를 보내.  
#iconic_button


pyautogui.alert("사람인걸 증명해주세요 ^^")  #사람인걸 증명해주세요 라는 창을 띄워주세요. 

elem = browser.find_element_by_css_selector(".button-blue.submit-button")  #브라우저를 대상으로 .button-blue.submit-button라는 css_selector로 된 element를 찾아서 elem에 대입  
elem.click() #elem를 클릭 

#print(pyautogui.position())
#전송 버튼을 클릭 


#mail_to 
#mail_subject
#mail_text